# Awesome HORIZON SHIELD

**The HORIZONs株式会社が運営する、データベース・MCPサーバー・検証台帳の全目録。**
**Every database, MCP server and verification ledger we operate — in one list, each row checkable by anyone.**

[![MCP](https://img.shields.io/badge/protocol-MCP-2f6feb)](https://modelcontextprotocol.io)
[![JCCDB DOI](https://img.shields.io/badge/JCCDB-10.5281%2Fzenodo.21898745-1682D4)](https://doi.org/10.5281/zenodo.21898745)
[![JHNRD DOI](https://img.shields.io/badge/JHNRD-10.5281%2Fzenodo.22083722-1682D4)](https://doi.org/10.5281/zenodo.22083722)
[![Register DOI](https://img.shields.io/badge/Conduct%20Register-10.5281%2Fzenodo.21970931-1682D4)](https://doi.org/10.5281/zenodo.21970931)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0000--9180--903X-A6CE39)](https://orcid.org/0009-0000-9180-903X)
[![Daily conduct measurements](https://img.shields.io/badge/conduct-measured%20daily-2ea043)](https://gate.horizonshield.dev/register)

これは「おすすめリスト」ではありません。**自社の棚卸しです。** 中立を装いません。
代わりに、全ての行に「他人が確かめる方法」を付けます。DOI、公式レジストリ、
毎日の死活測定、Bitcoin へのアンカー。**信じてもらう必要がないものだけを載せます。**

This is not a neutral "awesome list" — it is our own inventory, and we say so.
What makes it worth reading is that **every row carries a way for a stranger to check it**:
a DOI, an official registry entry, daily conduct measurements, or a Bitcoin anchor.

---

## 1. データベース / Open datasets

| | 中身 | 規模 | 検証 | ライセンス |
|---|---|---|---|---|
| **[JCCDB](https://github.com/ogasurfproject-jpg/japan-construction-cost-database)**<br>Japan Construction Cost Database | 建設・リフォームの実勢価格。過大請求の実測（平均83万円の水増し、最大282万円/84.9%超過） | 65,520 項目 | [DOI 10.5281/zenodo.21898745](https://doi.org/10.5281/zenodo.21898745) ・ [論文 10.31224/7007](https://doi.org/10.31224/7007) ・ Bitcoin Block #949356 | CC BY 4.0 |
| **[JHNRD](https://github.com/ogasurfproject-jpg/jhnrd)**<br>Japan Home-visit Nursing Reimbursement Database | 訪問看護の算定要件。数字ではなく、**数字がどこから来たか**の記録。全項目に出典と、その出典の格（法令/行政/二次）が付く | 33 項目・出典 26 件<br>**未確認 54 件を未確認と明記** | [DOI 10.5281/zenodo.22083722](https://doi.org/10.5281/zenodo.22083722) ・ [利益相反の開示](https://github.com/ogasurfproject-jpg/jhnrd/blob/main/GOVERNANCE.md) ・ CI が開示文の存在を毎回検査 | CC BY 4.0 |
| **[JIDEC](https://ledger.horizonshield.dev/llms.txt)**<br>公開検証台帳 (NENRIN) | 見積もり監査の記録を Bitcoin にアンカーした公開台帳。運営者にも改竄も削除もできない | — | OpenTimestamps ・ 各記録に再計算可能な SHA-256 | 読み取り自由 |

JHNRD の設計原則: **確認できないものは `confirmed:false` のまま出す。矛盾は両論のまま持つ。
探して無かったことも記録する。** 一資料を二度読んで一致しても、二資料の一致とは数えない。

---

## 2. 公開MCPサーバー / Public MCP servers

すべて [公式 MCP レジストリ](https://registry.modelcontextprotocol.io) に登録済み。Streamable HTTP。

| サーバー | レジストリ名 | エンドポイント | 言うこと / 決して言わないこと |
|---|---|---|---|
| **KIRA 適正診断** | `io.github.ogasurfproject-jpg/horizon-shield` | `https://mcp.horizonshield.dev/mcp` | 見積もりを JCCDB と照合し、整合スコアと危険信号を返す。**金額の正解は言わない** |
| **YAKUMO 加盟店ディレクトリ** | `io.github.ogasurfproject-jpg/hs-hearing` | `https://hearing.horizonshield.dev/mcp` | KIRA 監査を通過した施工店だけを返す。**価格は返さない。未検証店は施主に見せない（fail-closed）** |
| **KIRA 相談窓口 (WebMCP)** | `io.github.ogasurfproject-jpg/horizon-shield-webmcp` | `https://web.horizonshield.dev/mcp` | リフォームの相談の入口。1行の `<script>` でどのサイトにも埋め込める |
| **JIDEC 台帳** | `io.github.ogasurfproject-jpg/jidec` | `https://jidec.horizonshield.dev/mcp` | 監査記録の引用と、独立再検証の手順を返す。**信用を要求しない** |
| **JHNRD 公開MCP** | `io.github.ogasurfproject-jpg/jhnrd` | `https://jhnrd-mcp.oga-surf-project.workers.dev/mcp` | 算定要件と出典を返す。鍵なし・読み取り専用。**「算定できます」とは決して言わない**（要件と出典だけを返し、判断は返さない設計を、72件の自動検査が毎回確かめる） |
| **検証ゲート** | `io.github.ogasurfproject-jpg/hs-verify-gate` | `https://gate.horizonshield.dev/mcp` | 上の全部を毎日測る測定器。**自分自身も測定対象に入れている** |

## 3. 加盟店MCP / Per-member MCP servers

加盟店それぞれが、自分の名前で AI に応答する口を持つ。掲載条件は1つ:
**独立監査（KIRA）を通過していること。** 通過していない店は施主に出ない。

| | 状態 |
|---|---|
| No.001 リフォーム職人株式会社（愛知） | `https://p001.horizonshield.dev/mcp` — [測定履歴](https://gate.horizonshield.dev/history?endpoint=https%3A%2F%2Fp001.horizonshield.dev%2Fmcp) |
| No.002 ミネオトーヨー住器株式会社（神奈川） | `https://p002.horizonshield.dev/mcp` — [測定履歴](https://gate.horizonshield.dev/history?endpoint=https%3A%2F%2Fp002.horizonshield.dev%2Fmcp) |
| No.003（訪問看護・2026年10月 運用開始予定） | 準備中 — 建設と同じ検証規律を、医療・介護請求の領域に適用する最初の例 |

---

## 4. 検証の層 / The verification layer

ここが、このリストと普通の「awesome list」の違いです。

- **[MCP Conduct Register](https://github.com/ogasurfproject-jpg/mcp-conduct-register)** — 上のサーバー群の**行動記録**。毎日、公開APIから機械が作り直す。**行を選ぶ人間はいない。** 掲載枠は売っていない。運営者に不都合な記録も、消す経路がコードに存在しない。[DOI 10.5281/zenodo.21970931](https://doi.org/10.5281/zenodo.21970931)
- **[MCP Registry Survey](https://github.com/ogasurfproject-jpg/mcp-registry-survey)** — 2026-08-19 に公式レジストリ全 22,636 サーバーを実際に歩いた測量記録。自社を測る前に、世界の水準を測った
- **[検証ディレクトリ](https://shield.the-horizons-innovation.com/verify-directory/)** — 上記すべての人間向けの入口

### 自分で確かめる / Verify any row yourself

```bash
# どのサーバーの行動記録でも、そのまま取れる
curl -s "https://gate.horizonshield.dev/register"
# 1台ぶんの履歴と record_sha256（自分で再計算して比べられる）
curl -s "https://gate.horizonshield.dev/history?endpoint=https://mcp.horizonshield.dev/mcp"
```

---

## 5. 利益相反 / Conflict of interest

運営は The HORIZONs株式会社（監修: 大賀俊勝、建設業30年、[ORCID 0009-0000-9180-903X](https://orcid.org/0009-0000-9180-903X)）。
**弊社は有償のサービスを販売しています。** つまりこの目録には、載せる側の都合が働き得ます。
だからこそ、どの行も「弊社を信じずに確かめる方法」と一緒に置いています。
JHNRD の開示文は [GOVERNANCE.md](https://github.com/ogasurfproject-jpg/jhnrd/blob/main/GOVERNANCE.md) にあり、
その存在自体を CI が毎回検査しています（消すとビルドが落ちる）。

## License

この目録の文章: CC BY 4.0。各行のリンク先は、それぞれのライセンスに従います。
機械可読版: [`catalog.json`](./catalog.json)
