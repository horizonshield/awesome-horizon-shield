# How to take part

This catalog is the operator's own inventory, and **nobody adds a row by hand** — not even us.
A server earns a row by being *measured*; the register writes it. So the usual "open a PR to add
my tool" does not apply here. There are three real ways to take part, and each one keeps the list
honest instead of longer.

<sub>この目録は運営者自身の在庫であり、行は手で足さない。サーバは「測られて」載る。だから普通の「PRで自分のツールを足す」は通らない。参加の道は次の3つ。</sub>

---

## 1. Get listed — earn your own endpoint

**Who:** contractors, renovation firms, one-person shops, and (from Oct 2026) home-visit nursing
operators who want a verified page a customer can *check*, not just read.

**The one condition:** pass the independent **KIRA** fair-price audit. It checks your estimates
against the 65,520 items in [JCCDB](https://github.com/ogasurfproject-jpg/japan-construction-cost-database)
and flags padding, using the same instrument as every row already on the list. **No pass, no listing.**

**What you get when you pass:**

- your own MCP endpoint, `https://p0NN.horizonshield.dev/mcp`, that answers **in your name**;
- a **public conduct history the [gate](https://gate.horizonshield.dev/register) rebuilds daily —
  that you cannot edit**;
- a place in the [YAKUMO verified contractor directory](https://hearing.horizonshield.dev/mcp),
  which never shows an unverified store to a homeowner (fail-closed).

**Why it is worth it:** your customers get a page about you that **you can't spin**. That is precisely
why it is believed. A review you wrote is worth nothing; a measurement you can't touch is worth everything.

**Start:** open a [**Request a listing**](../../issues/new?template=request-listing.yml) issue.
The desk (担当: 大賀) takes it from there. We never quote a price or promise a result inside an
automated reply — a person does that.

<sub>載る条件はひとつ、独立したKIRA監査を通ること。通れば、あなたの名前で答える口・あなたが編集できない日次の素行記録・不正店を施主に見せない検証済み名簿への掲載が付く。自分で書いたレビューは無価値、動かせない測定値は決定的。</sub>

---

## 2. Falsify us — find what we got wrong

We would rather publish a mistake than hide one.

If a row won't verify, a number won't reproduce, or a source doesn't say what we claim, open a
[**Falsification report**](../../issues/new?template=falsification.yml). Show what you checked and
what you got — a `curl`, a DOI, a statute reference, a recomputed `record_sha256`.

- **Confirmed findings are kept in the open, with credit.** The code contains no route to quietly
  drop a record that embarrasses us — that rule is the whole point of the list.
- This is not a bounty paid in money. It is paid in the only currency this catalog runs on:
  **being checkable.**

<sub>確かめられない行・再現しない数字・出典と食い違う記述を見つけたら Falsification report を。確認できた指摘はクレジット付きで公開のまま残す。恥ずかしい記録を消す経路はコードに無い。</sub>

---

## 3. Fix the plumbing — typos, links, clarity

Plain documentation fixes are welcome as ordinary pull requests: a broken link, a typo, a clearer
sentence, an accessibility improvement on the website. Two lines that never move by PR:

- **the numbers** — JHNRD's counts come from its own `status.json` (emitted by `tools/validate.py`);
  JCCDB's item count from its release. We quote the owner's figures and never recount them here.
- **the live block** — everything between `<!-- LIVE:START -->` and `<!-- LIVE:END -->` in
  `README.md`, and the two files in `badges/`, are written only by
  [`scripts/refresh.py`](scripts/refresh.py). Don't hand-edit them; they are rebuilt daily from the
  public register, and a stale date is honest while an invented row is not.

---

## What we don't do

- We don't add a server because it asked nicely, or because it starred us. Rows are measured, not granted.
- We don't sell placement. There is no code path to add or remove a row for money.
- We don't let an automated reply quote a price, a制度, or a contract. Those go to a human (大賀).
- We don't recount someone else's dataset to make our number look rounder.

Operated by The HORIZONs K.K. · supervised by Toshikatsu Oga
([ORCID 0009-0000-9180-903X](https://orcid.org/0009-0000-9180-903X)) ·
conflict of interest disclosed in
[JHNRD GOVERNANCE.md](https://github.com/ogasurfproject-jpg/jhnrd/blob/main/GOVERNANCE.md).
