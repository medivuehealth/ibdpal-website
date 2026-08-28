/**
 * Server-side profanity / vulgar / obscene language check for reader submissions.
 * Whole-word and compact (leetspeak) matching. Not exhaustive; blocks common abuse.
 */

const BLOCKED_WORDS = new Set(
  `
  ass asshole assholes bastard bastards bitch bitches bitchy bollocks bullshit
  clit cock cocks cunt cunts damn dick dicks douche douchebag fag faggot fags
  fuck fucked fucker fuckers fucking fucks goddamn hell jackass jerk motherfucker
  nigga nigger piss pissed prick pussies pussy shit shits shitty slut sluts
  twat wank wanker whore whores asshat asswipe bimbo boner boob boobs bukkake
  cameltoe clitoris cum cumming cumshot dildo dyke erection felching felch
  felatio fellatio fistfuck gangbang genitals handjob hentai hooker horniest
  horny incest jackoff jerkoff jizz kike kinky labia masturbate masturbating
  masturbation milf molest molestation molester moron nazi negro nipple nipples
  orgasm orgy pedo pedophile pedophilia penis porn porno pornography pussies
  rapist rectum retard retarded rimjob scrotum sex sexy sh1t slutty sodom
  sodomy spic spunk testicle testicles tit tits titties titty tranny turd
  vagina vibrator voyeur vulva wank wanker wetback wop xxx
  `
    .trim()
    .split(/\s+/)
);

const BLOCKED_PATTERNS = [
  /\bf+u+c+k+\w*/i,
  /\bs+h+i+t+\w*/i,
  /\bb+i+t+c+h+\w*/i,
  /\bc+u+n+t+\w*/i,
  /\ba+s+s+h+o+l+e+\w*/i,
  /\bd+i+c+k+\w*/i,
  /\bp+u+s+s+y+\w*/i,
  /\bn+i+g+g+\w*/i,
  /\bf+a+g+\w*/i,
  /\br+e+t+a+r+d+\w*/i,
  /\bwh+o+r+e+\w*/i,
  /\bs+l+u+t+\w*/i,
  /\brap+e+\w*/i,
  /\bped+o+\w*/i,
];

function tokenize(text) {
  return String(text || '')
    .toLowerCase()
    .split(/[^a-z0-9']+/i)
    .map((w) => w.replace(/^'+|'+$/g, ''))
    .filter(Boolean);
}

function compactLetters(value) {
  return String(value || '')
    .toLowerCase()
    .replace(/[^a-z0-9]/g, '');
}

export function containsProfanity(text) {
  const raw = String(text || '').trim();
  if (!raw) return false;

  for (const pattern of BLOCKED_PATTERNS) {
    if (pattern.test(raw)) return true;
  }

  const tokens = tokenize(raw);
  for (const token of tokens) {
    if (BLOCKED_WORDS.has(token)) return true;
    const stem = token.replace(/(ing|ed|s|es|er|ers|ly)$/i, '');
    if (stem.length >= 4 && BLOCKED_WORDS.has(stem)) return true;
  }

  const compact = compactLetters(raw);
  if (compact.length >= 4) {
    for (const pattern of BLOCKED_PATTERNS) {
      if (pattern.test(compact)) return true;
    }
  }

  return false;
}

export function profanityErrorMessage() {
  return 'Please remove vulgar, profane, or obscene language and try again.';
}
