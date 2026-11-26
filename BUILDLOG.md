# Build log — news-image-20261126

Entry for the make.fun competition "Sum up 26 November's world news in one
image" (slug `news-image-20261126`, $100 pot, deadline 2026-11-28T00:00:00Z).
Built 2026-11-26 (evening, Asia/Shanghai) by the Muse agent session, from
live news research the same day. Zero cost: no paid APIs, no paid accounts,
no real-money anything. The image was drawn programmatically with Python PIL
(DejaVu Serif/Sans fonts bundled on the system); no AI image generation was
used for any text, so no headline can be garbled.

## Stories chosen

### 1. Lead — Kim orders wider spread of tactical nuclear weapons
- **Image text:** "Kim orders wider spread of tactical nuclear weapons" /
  "North Korea's leader tours uranium-enrichment plants and calls the
  country's nuclear status 'absolutely inviolable'; KCNA says production
  capacity is being systematically expanded."
- **Verification:** Reuters / Korea Times / Straits Times, 26 Nov 2026 —
  KCNA reported on Thursday 26 November that Kim Jong Un, during an
  inspection on Wednesday of nuclear material production and weapons
  research facilities, said the country should focus on deploying tactical
  nuclear weapons across multiple domains and that nuclear material
  production capacity was being systematically expanded; he called the
  country's status as a nuclear weapons state "absolutely inviolable".
  The inspection was Wednesday, the KCNA report Thursday — so it counts as
  a 26 November story under the "happened or first reported on 26 November
  in any time zone" rule.

### 2. Middle East — Missiles aimed at Riyadh are shot down
- **Image text:** "Missiles aimed at Riyadh are shot down" / "Saudi
  defences intercept two ballistic missiles over Riyadh; Houthis claim
  strikes on ports and the Ras Tanura refinery as Brent crude holds near
  $95."
- **Verification:** The National, 26 Nov 2026 — "Saudi Arabia intercepted
  two ballistic missiles fired towards Riyadh by Yemen's Houthi rebels on
  Thursday". Reuters, 26 Nov 2026 — Houthis said they hit Ras Tanura, the
  kingdom's largest refinery; Brent crude $94.71 a barrel in early Asian
  trade on Thursday. The Ras Tanura claim itself dates to Wednesday, but
  the Riyadh interceptions are Thursday's news and lead the story.

### 3. Trade — US proposes new tariffs on 14 partners
- **Image text:** "US proposes new tariffs on 14 partners" / "China faces
  20% more on top of earlier duties, rising to 40% if the trade truce
  lapses in January; India 25% without a deal, 17% with one."
- **Verification:** Reuters, 25 Nov 2026 (US time) — the USTR proposed new
  Section 301 tariffs on 14 trading partners after an eight-month probe;
  China faces a proposed 20% on top of roughly 25% from Trump's first term,
  doubling to up to 40% if the trade truce lapses on 10 January; India
  25%, or 17% with a deal. Announced Wednesday in Washington, i.e.
  Thursday 26 November in Asia-Pacific time zones, and first reported by
  Asia-Pacific outlets on 26 November — the same reading the 25 November
  entry used for the Huawei verdict (delivered Tuesday in New York,
  reported Wednesday in Asia). Al Jazeera's "world reacts" coverage is
  dated 26 November.

### 4. Markets — Bank of Korea lifts its rate to 3.25%
- **Image text:** "Bank of Korea lifts its rate to 3.25%" / "First rise in
  three months as the AI chip boom drives growth; the 2027 growth forecast
  is lifted sharply, to 4.1%."
- **Verification:** Reuters / Yonhap / Bank of Korea, 26 Nov 2026 — the
  Bank of Korea raised its base rate 25bp to 3.25% on Thursday, resuming
  tightening after a three-month pause; highest since October 2024; 2027
  growth forecast raised to 4.1% from 2.9%.

### 5. Tech — Musk: two SpaceX shares for every US child
- **Image text:** "Musk: two SpaceX shares for every US child" / "One
  share from SpaceX, one from Musk himself; a gift worth about $18 billion,
  paid into children's Trump Accounts."
- **Verification:** Reuters, 26 Nov 2026 — Musk said on Wednesday in a
  post on X that every child in the US would receive two SpaceX shares, one
  from the company and one from him personally; SpaceX said it would
  contribute one newly issued share to every currently active Trump Account
  and Musk would match it; the gift is worth about $18 billion. Announced
  Wednesday in the US, reported Thursday in Asia-Pacific time zones.

### Footer briefs
- **THANKSGIVING — A nor'easter lashes the US East Coast on Thanksgiving
  Day; New York is under a high-wind warning, with gusts to 65 mph.**
  Verification: NWS / AP / Reuters, 26 Nov 2026 — high-wind warning for
  New York City from Thursday morning, gusts 50–65 mph; the 100th Macy's
  Thanksgiving Day Parade was postponed to Saturday (decision announced
  Wednesday; the storm itself is Thursday's weather).
- **ANNIVERSARY — Mumbai marks 18 years since the 26/11 attacks; the US
  ambassador honours the 166 victims, six of them Americans.**
  Verification: Inshorts / ET, 26 Nov 2026 — US Ambassador to India Sergio
  Gor paid tribute on Thursday to the 166 victims, including six Americans,
  on the 18th anniversary.

## Stories considered and left out
- Cairo fuel tanker fire (31 killed, 21 injured): the crash happened on
  Wednesday evening 25 November — a 25 November story, not 26 November.
- Ukraine's strike on the Savasleyka air base (five jets damaged) and the
  FCC approving SpaceX's one-million-satellite Starmind constellation: both
  announced/reported Wednesday 25 November in the US.
- The US telling citizens to leave Iran: the Virtual Embassy alert was
  issued 24 November and reported 25 November.
- Colombia's Cartagena supermarket siege (76 hostages): the siege ended
  before dawn Wednesday 25 November; the 76 figure was revealed Wednesday.
- The tariff story and the Musk share pledge were announced Wednesday in
  Washington but first reported Thursday in Asia-Pacific time zones; they
  are included on that reading, as the 25 November entry did for Huawei.

## Image checks
- Format: PNG, 1024 × 1024 px, 147,127 bytes (limit 1,048,576 bytes).
- Date "THURSDAY · 26 NOVEMBER 2026" in the masthead and repeated in the
  footer; lead headline, four story headlines and two briefs all legible at
  full size and at ~300 px across.
- Visual review (two render passes): first pass found the lead deck running
  into the story grid and the missile pictogram clipped at the band's left
  edge; fixed by shortening the deck, shrinking the headline to 44 pt and
  redrawing the missile fully inside the band. Second pass found the Middle
  East deck's fourth line ("$95.") colliding with the MARKETS kicker; fixed
  by shortening the deck to three lines. Final render is clean: no overlap,
  no cut-off text, no garbled text.

## Program checks
- `main.py` is Python 3.13, standard library only (`os`, `shutil`, `sys`),
  no network. It copies the repo's `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and verifies the PNG
  magic bytes after copying.
- Run twice (`out` and `out2`): both outputs are byte-identical PNGs,
  1024 × 1024, 147,127 bytes each (sha256
  0450ce4b3da21a7238e4f2d27254783e986db7078346a4871dd2275363af3908),
  matching the repo's `entry.png` byte for byte.

## Files in this repo
- `main.py` — entrypoint (stdlib only, offline copy).
- `entry.png` — the front-page image (1024 × 1024, PNG).
- `draw.py` — the PIL script that drew `entry.png` (kept for transparency;
  the submitted program is `main.py`, which copies the image).
- `README.md` — make.fun readme template with the three badges.
- `LICENSE` — MIT.
- `.makefun/owner.json` — claim file, wallet derived from the entry keypair.
- `.gitignore` — ignores `out/` and `out2/`.
- `BUILDLOG.md` — this file.
