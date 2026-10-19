#!/usr/bin/env python3
"""Update YouTube view counts in K/KTV.md (run daily via GitHub Actions)."""
import json
import os
import re
import sys
import urllib.request

MD_PATH = "K/KTV.md"
API_URL = "https://www.googleapis.com/youtube/v3/videos"


def main():
    key = os.environ.get("YOUTUBE_API_KEY")
    if not key:
        sys.exit("error: YOUTUBE_API_KEY is not set")
    md = open(MD_PATH, encoding="utf-8").read()
    ids = sorted(set(re.findall(r"https://youtu\.be/([\w-]{11})", md)))
    print(f"found {len(ids)} video ids")
    views = {}
    for i in range(0, len(ids), 50):
        chunk = ",".join(ids[i : i + 50])
        url = f"{API_URL}?part=statistics&id={chunk}&key={key}"
        with urllib.request.urlopen(url) as r:
            data = json.load(r)
        if "error" in data:
            sys.exit(f"API error: {data['error'].get('message')}")
        for item in data.get("items", []):
            views[item["id"]] = item["statistics"]["viewCount"]
    print(f"got counts for {len(views)} videos")
    changed = 0
    out = []
    for line in md.splitlines(keepends=True):
        m = re.search(r"https://youtu\.be/([\w-]{11})", line)
        if m and m.group(1) in views:
            body = line.rstrip("\n")
            new_body, n = re.subn(r"\| (\d+) \|$", f"| {views[m.group(1)]} |", body)
            if n:
                changed += 1
                line = new_body + ("\n" if line.endswith("\n") else "")
        out.append(line)
    open(MD_PATH, "w", encoding="utf-8").write("".join(out))
    print(f"updated {changed} rows in {MD_PATH}")


main()
