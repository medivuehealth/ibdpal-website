import { cleanText, json, methodNotAllowed, parseBody } from '../_web-db.js';

const GEMINI_MODEL = 'gemini-2.5-flash';
const MAX_FIELD_LENGTH = 500;

function fallbackRecipes(goal, ingredients) {
  const ingredientText = ingredients || 'simple pantry staples';
  return [
    {
      title: 'Gentle Rice Bowl Idea',
      whyItMayFit: `Uses ${ingredientText} in a simple, lower-spice format that some people prefer on sensitive days.`,
      ingredients: ['Cooked rice or another tolerated grain', 'Plain protein such as chicken, tofu, or egg', 'Soft cooked carrots or another tolerated vegetable', 'Small amount of olive oil or broth'],
      steps: ['Cook ingredients until soft and easy to chew.', 'Keep seasoning mild.', 'Serve small portions and adjust based on personal tolerance.'],
      ibdNote: 'This is education only, not medical advice. Personal food tolerance varies with Crohn\'s, colitis, strictures, surgery history, and flare status.',
      youtubeQueries: ['gentle rice bowl meal prep', 'plain chicken rice bowl recipe']
    }
  ];
}

function stripCodeFence(value) {
  return String(value || '')
    .replace(/^```(?:json)?/i, '')
    .replace(/```$/i, '')
    .trim();
}

function parseGeminiJson(text) {
  const clean = stripCodeFence(text);
  try {
    return JSON.parse(clean);
  } catch {
    const match = clean.match(/\{[\s\S]*\}/);
    if (!match) return null;
    try {
      return JSON.parse(match[0]);
    } catch {
      return null;
    }
  }
}

function normalizeRecipe(recipe) {
  return {
    title: cleanText(recipe?.title, 90) || 'Gentle recipe idea',
    whyItMayFit: cleanText(recipe?.whyItMayFit, 240) || 'A simple idea to review against personal tolerance and care-team guidance.',
    ingredients: Array.isArray(recipe?.ingredients) ? recipe.ingredients.slice(0, 10).map((item) => cleanText(item, 90)).filter(Boolean) : [],
    steps: Array.isArray(recipe?.steps) ? recipe.steps.slice(0, 8).map((item) => cleanText(item, 160)).filter(Boolean) : [],
    ibdNote: cleanText(recipe?.ibdNote, 260) || 'Education only. Ask your GI clinician or dietitian about personal restrictions.',
    youtubeQueries: Array.isArray(recipe?.youtubeQueries) ? recipe.youtubeQueries.slice(0, 3).map((item) => cleanText(item, 90)).filter(Boolean) : []
  };
}

function systemPrompt() {
  return [
    'You generate cautious recipe ideas for an IBD education website.',
    'Do not diagnose, treat, promise symptom control, or identify food triggers.',
    'Do not say a recipe is safe for Crohn\'s disease, ulcerative colitis, strictures, ostomies, pregnancy, children, or flares.',
    'Use phrases like "may be easier for some people" and "personal tolerance varies."',
    'Avoid alcohol. Avoid extreme claims. Keep seasonings gentle unless the user asks otherwise.',
    'If severe symptoms are mentioned, include a note to contact a clinician or urgent care.',
    'Return strict JSON only with this shape: {"recipes":[{"title":"","whyItMayFit":"","ingredients":[],"steps":[],"ibdNote":"","youtubeQueries":[]}],"disclaimer":""}.',
    'Create 2 recipes and 2-3 YouTube search queries per recipe. YouTube queries should be general cooking searches, not medical advice.'
  ].join('\n');
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return methodNotAllowed(res, ['POST']);
  }

  const apiKey = process.env.IBDPAL_GEMINI;
  if (!apiKey) {
    return json(res, 200, {
      success: true,
      fallback: true,
      disclaimer: 'Recipe ideas are educational and are not medical advice.',
      recipes: fallbackRecipes('', '')
    });
  }

  try {
    const body = parseBody(req);
    const goal = cleanText(body.goal, 80) || 'general gentle meal idea';
    const ingredients = cleanText(body.ingredients, MAX_FIELD_LENGTH) || '';
    const avoid = cleanText(body.avoid, MAX_FIELD_LENGTH) || '';
    const notes = cleanText(body.notes, MAX_FIELD_LENGTH) || '';

    if (!ingredients && !goal) {
      return json(res, 400, {
        success: false,
        error: 'Add a goal or ingredients to generate recipe ideas.'
      });
    }

    const userPrompt = [
      `Goal: ${goal}`,
      `Ingredients available: ${ingredients || 'not specified'}`,
      `Avoid or limit: ${avoid || 'not specified'}`,
      `Context notes: ${notes || 'not specified'}`
    ].join('\n');

    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent?key=${encodeURIComponent(apiKey)}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        systemInstruction: {
          parts: [{ text: systemPrompt() }]
        },
        contents: [
          {
            role: 'user',
            parts: [{ text: userPrompt }]
          }
        ],
        generationConfig: {
          temperature: 0.45,
          maxOutputTokens: 1800,
          responseMimeType: 'application/json'
        }
      })
    });

    if (!response.ok) {
      throw new Error(`Gemini request failed: ${response.status}`);
    }

    const payload = await response.json();
    const text = payload?.candidates?.[0]?.content?.parts?.map((part) => part.text || '').join('\n') || '';
    const parsed = parseGeminiJson(text);
    const recipes = Array.isArray(parsed?.recipes) ? parsed.recipes.map(normalizeRecipe).filter((recipe) => recipe.title).slice(0, 2) : [];

    if (!recipes.length) {
      throw new Error('Gemini returned no parseable recipes.');
    }

    return json(res, 200, {
      success: true,
      model: GEMINI_MODEL,
      disclaimer: cleanText(parsed?.disclaimer, 260) || 'Recipe ideas are educational and are not medical advice. Ask your GI clinician or dietitian about personal restrictions.',
      recipes
    });
  } catch (error) {
    console.error('recipe-suggestions error', error);
    const body = parseBody(req);
    return json(res, 200, {
      success: true,
      fallback: true,
      disclaimer: 'Recipe AI is temporarily unavailable. These fallback ideas are educational and are not medical advice.',
      recipes: fallbackRecipes(cleanText(body.goal, 80), cleanText(body.ingredients, 160))
    });
  }
}
