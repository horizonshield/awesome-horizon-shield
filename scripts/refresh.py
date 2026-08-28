#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Refresh the live block of README.md from the public gate API.

No curation. The script fetches whatever the register returns and formats every row.
If the API is unreachable it changes nothing and exits 0: a stale table is honest,
an invented one is not. That rule is copied deliberately from mcp-conduct-register,
where it was written first.

  python3 scripts/refresh.py
"""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

REGISTER_URL = "https://gate.horizonshield.dev/register"
README = "README.md"
START = "<!-- LIVE:START -->"
END = "<!-- LIVE:END -->"
BADGE_VERIFIED = "badges/verified.json"
BADGE_SERVERS = "badges/servers.json"

# 目録に載せている口だけを、生きているかどうかの数に入れる。
# 他所の口をこの数に混ぜると、自分の成績を他人の成績で薄めることになる。
OURS = (
    "mcp.horizonshield.dev",
    "hearing.horizonshield.dev",
    "web.horizonshield.dev",
    "jidec.horizonshield.dev",
    "gate.horizonshield.dev",
    "p001.horizonshield.dev",
    "p002.horizonshield.dev",
    "jhnrd-mcp.oga-surf-project.workers.dev",
    "femtech.horizonshield.dev",
)


def fetch():
    req = urllib.request.Request(
        REGISTER_URL,
        headers={"user-agent": "awesome-horizon-shield/1.0 (+https://github.com/ogasurfproject-jpg/awesome-horizon-shield)"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def is_ours(endpoint):
    return any(h in endpoint for h in OURS)


def build_table(rows, stamp):
    out = []
    out.append("Rebuilt from <https://gate.horizonshield.dev/register> at **%s**." % stamp)
    out.append("")
    out.append("Nobody chooses these rows. A verdict of `verified` means the conditions that")
    out.append("were measured passed on that date. It does not mean the numbers a server")
    out.append("returns are correct, and absence is **not** a negative verdict.")
    out.append("")
    out.append("| Server | Endpoint | Latest verdict | Measured | Measurements | record_sha256 |")
    out.append("|---|---|---|---|---|---|")
    for r in rows:
        ep = r.get("endpoint") or ""
        label = r.get("operator_label") or {}
        name = label.get("en") or label.get("ja") or ep
        latest = r.get("latest") or {}
        verdict = latest.get("status") or "not measured yet"
        mark = {"verified": "🟢", "pending": "🟡", "failed": "🔴"}.get(verdict, "⚪")
        when = (latest.get("at") or "")[:10]
        n = r.get("measurements")
        sha = (latest.get("record_sha256") or "")[:12]
        hist = r.get("history_url") or ""
        ep_cell = "[`%s`](%s)" % (ep, hist) if hist else "`%s`" % ep
        out.append("| %s | %s | %s %s | %s | %s | `%s` |" % (
            name, ep_cell, mark, verdict, when, n if isinstance(n, int) else "?", sha))
    return "\n".join(out)


def write_badge(path, label, message, color):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"schemaVersion": 1, "label": label, "message": message, "color": color},
                  f, ensure_ascii=False)
        f.write("\n")


def main():
    try:
        data = fetch()
    except Exception as e:
        print("register unreachable: %s" % e, file=sys.stderr)
        print("Nothing changed. A stale table is honest, an invented one is not.", file=sys.stderr)
        return 0

    rows = data.get("rows") or []
    if not rows:
        print("register returned no rows; nothing changed.", file=sys.stderr)
        return 0

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    body = build_table(rows, stamp)

    src = open(README, encoding="utf-8").read()
    if START not in src or END not in src:
        print("markers missing in README", file=sys.stderr)
        return 1
    new = re.sub(re.escape(START) + r".*?" + re.escape(END),
                 START + "\n" + body + "\n" + END, src, flags=re.S)
    if new != src:
        open(README, "w", encoding="utf-8").write(new)

    ours = [r for r in rows if is_ours(r.get("endpoint") or "")]
    ok = sum(1 for r in ours if ((r.get("latest") or {}).get("status") == "verified"))
    total = len(ours)
    # 全部緑でなければ緑と言わない。言ったら、この目録自体が測っていないことになる。
    color = "2ea043" if (total and ok == total) else ("d29922" if ok else "cf222e")
    write_badge(BADGE_VERIFIED, "conduct", "%d/%d verified · %s" % (ok, total, stamp[:10]), color)
    write_badge(BADGE_SERVERS, "endpoints measured", str(total), "2f6feb")

    print("rows=%d ours=%d verified=%d at %s" % (len(rows), total, ok, stamp))
    return 0


if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    sys.exit(main())
