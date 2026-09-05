"""
Re-download Part VI food images from curated Unsplash/Pexels URLs.
Only replaces files that are listed in CORRECTED_URLS.
Usage: python scripts/fix_part6_food_images.py
"""
from __future__ import annotations

import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "blogs" / "assets"

# Curated free-license photos verified to match the food name.
# Prefer Unsplash License images via images.unsplash.com CDN.
CORRECTED_URLS: dict[str, str] = {
    # Confirmed mismatches / duplicates
    "sweet-potato-ibd": "https://images.unsplash.com/photo-1570723735746-c9bd51bd7c40?auto=format&fit=crop&w=1200&q=80",
    "peanut-butter-ibd": "https://images.unsplash.com/photo-1668440241140-1af5bce424c4?auto=format&fit=crop&w=1200&q=80",
    "turkey-ibd": "https://images.unsplash.com/photo-1574672280600-4accfa5b6f98?auto=format&fit=crop&w=1200&q=80",
    "tuna-ibd": "https://images.unsplash.com/photo-1580959375944-abd7eb977c7d?auto=format&fit=crop&w=1200&q=80",
    "tofu-ibd": "https://images.unsplash.com/photo-1760228865341-675704c22a5b?auto=format&fit=crop&w=1200&q=80",
    "kimchi-ibd": "https://images.unsplash.com/photo-1583224964978-240ee87d0b6b?auto=format&fit=crop&w=1200&q=80",
    "bone-broth": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=1200&q=80",
    "congee-ibd": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=1200&q=80",
    "couscous-ibd": "https://images.unsplash.com/photo-1516684668137-632fa0f0a5a0?auto=format&fit=crop&w=1200&q=80",
    "miso-ibd": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=1200&q=80",
    # Likely swapped or weak matches — refresh from intended food photos
    "onion-garlic-ibd": "https://images.unsplash.com/photo-1518977956812-cd3dbadaaf31?auto=format&fit=crop&w=1200&q=80",
    "white-bread-ibd": "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=1200&q=80",
    "tortilla-ibd": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=1200&q=80",
    "eggs-ibd": "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?auto=format&fit=crop&w=1200&q=80",
    "paneer-ibd": "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=1200&q=80",
    "dal-ibd": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=1200&q=80",
    "chapati-ibd": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=1200&q=80",
    "dates-ibd": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?auto=format&fit=crop&w=1200&q=80",
    "plantain-ibd": "https://images.pexels.com/photos/3024866/pexels-photo-3024866.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "greek-yogurt-ibd": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=1200&q=80",
    "coffee-ibd": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=1200&q=80",
    "tea-ibd": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=1200&q=80",
    "salmon-ibd": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=1200&q=80",
    "chicken-ibd": "https://images.unsplash.com/photo-1598103442097-8b74394b95c6?auto=format&fit=crop&w=1200&q=80",
    "potato-ibd": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&w=1200&q=80",
    "white-rice-ibd": "https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?auto=format&fit=crop&w=1200&q=80",
    "oatmeal-ibd": "https://images.unsplash.com/photo-1517673400267-0251440c45dc?auto=format&fit=crop&w=1200&q=80",
    "chocolate-ibd": "https://images.unsplash.com/photo-1511381939415-e44015466834?auto=format&fit=crop&w=1200&q=80",
    "lean-beef-ibd": "https://images.unsplash.com/photo-1588168333986-5078d3ae3976?auto=format&fit=crop&w=1200&q=80",
    "banana-ibd": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=1200&q=80",
    "apple-ibd": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=1200&q=80",
    "blueberries-ibd": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&fit=crop&w=1200&q=80",
    "avocado-ibd": "https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?auto=format&fit=crop&w=1200&q=80",
    "melon-ibd": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=1200&q=80",
    "grapes-ibd": "https://images.unsplash.com/photo-1596363505729-4190a9506133?auto=format&fit=crop&w=1200&q=80",
    "strawberries-ibd": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&fit=crop&w=1200&q=80",
    "oranges-ibd": "https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&fit=crop&w=1200&q=80",
    "carrots-ibd": "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?auto=format&fit=crop&w=1200&q=80",
    "zucchini-ibd": "https://images.pexels.com/photos/128420/pexels-photo-128420.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "cucumber-ibd": "https://images.unsplash.com/photo-1449300079323-02e209d9d3a6?auto=format&fit=crop&w=1200&q=80",
    "spinach-ibd": "https://images.unsplash.com/photo-1576045057995-568f588f82fb?auto=format&fit=crop&w=1200&q=80",
    "broccoli-ibd": "https://images.unsplash.com/photo-1459411621453-7b03977f4bfc?auto=format&fit=crop&w=1200&q=80",
    "tomato-ibd": "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=1200&q=80",
    "corn-ibd": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?auto=format&fit=crop&w=1200&q=80",
}


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "IBDPalFoodImageFix/1.0 (educational nonprofit; contact info@ibdpal.org)",
            "Accept": "image/jpeg,image/*;q=0.8,*/*;q=0.5",
        },
    )
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
        data = resp.read()
    if len(data) < 5000:
        raise RuntimeError(f"Too small ({len(data)} bytes) for {dest.name}")
    if not (data[:3] == b"\xff\xd8\xff" or data[:8] == b"\x89PNG\r\n\x1a\n"):
        raise RuntimeError(f"Not an image for {dest.name}: {data[:40]!r}")
    dest.write_bytes(data)


def main() -> int:
    ok = 0
    for asset_dir, url in CORRECTED_URLS.items():
        dest = ASSETS / asset_dir / f"{asset_dir}_1.jpg"
        # bone-broth uses bone-broth_1.jpg
        if asset_dir == "bone-broth":
            dest = ASSETS / "bone-broth" / "bone-broth_1.jpg"
        try:
            download(url, dest)
            print(f"OK  {dest.relative_to(ROOT)} ({dest.stat().st_size} bytes)")
            ok += 1
        except Exception as exc:
            print(f"FAIL {asset_dir}: {exc}")
    print(f"Downloaded {ok}/{len(CORRECTED_URLS)}")
    return 0 if ok == len(CORRECTED_URLS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
