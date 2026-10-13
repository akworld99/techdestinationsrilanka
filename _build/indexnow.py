"""Tell Bing (and other IndexNow engines) which pages changed. Run by .github/workflows/indexnow.yml after each Pages deploy.

Submits pages touched by the last commit plus any page whose sitemap lastmod is from the last two days.
Set ALL=true to submit every URL in the sitemap.
"""
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
ROOT = Path(__file__).resolve().parent.parent
SITE_URL = "https://techdestinationsrilanka.lk"
KEY = "7c1e5a9d3b8f4e62a0d7c4b19f3e8a56"

sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
entries = dict(re.findall(r"<loc>(.*?)</loc><lastmod>(.*?)</lastmod>", sitemap))

if os.environ.get("ALL", "").lower() == "true":
    urls = set(entries)
else:
    recent = (date.today() - timedelta(days=2)).isoformat()
    urls = {u for u, d in entries.items() if d >= recent}
    try:
        changed = subprocess.run(["git", "diff", "--name-only", "HEAD~1", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    except subprocess.CalledProcessError:
        changed = []
    for f in changed:
        if f.endswith("index.html"):
            u = f"{SITE_URL}/{f[:-len('index.html')]}"
            if u in entries:
                urls.add(u)
        elif f == "llms.txt":
            urls.add(f"{SITE_URL}/llms.txt")

if not urls:
    print("Nothing changed, nothing to submit.")
    sys.exit(0)

payload = {"host": SITE_URL.split("//")[1], "key": KEY, "keyLocation": f"{SITE_URL}/{KEY}.txt", "urlList": sorted(urls)[:10000]}
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=json.dumps(payload).encode("utf-8"),
                             headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow accepted {len(urls)} URLs: HTTP {r.status}")
except urllib.error.HTTPError as err:
    print(f"IndexNow returned HTTP {err.code}: {err.read().decode('utf-8', 'replace')[:300]}")
    sys.exit(1 if err.code not in (200, 202) else 0)
for u in sorted(urls):
    print(" ", u)
