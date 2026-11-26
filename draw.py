# Draw the front page for news-image-20261126 with Python PIL.
# A newspaper front page summing up Thursday 26 November 2026.
# All text is drawn with DejaVu fonts, so no headline can be garbled.
# Run: python3 draw.py  -> writes entry.png (1024x1024) beside this file.

import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (26, 26, 26)
RED = (178, 34, 34)
GREY = (110, 108, 100)
RULE = (26, 26, 26)
NAVY = (28, 48, 92)
TEAL = (18, 92, 86)
GOLD = (176, 124, 22)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_para(draw, x, y, max_w, text, fnt, fill=INK, leading=None):
    lines = wrap(draw, text, fnt, max_w)
    lh = leading or int(fnt.size * 1.32)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

M = 44  # margin
# ---- masthead ----
d.rectangle([0, 0, W, 118], fill=(26, 26, 26))
d.text((M, 22), "THE WORLD TODAY", font=font(SERIF_B, 58), fill=(247, 243, 234))
d.text((W - M - d.textlength("No. 331", font=font(SANS, 20)), 30),
       "No. 331", font=font(SANS, 20), fill=(200, 196, 186))
d.text((W - M - d.textlength("ONE DAY · ONE PAGE", font=font(SANS, 20)), 58),
       "ONE DAY · ONE PAGE", font=font(SANS, 20), fill=(200, 196, 186))
d.line([M, 118, W - M, 118], fill=RULE, width=3)
d.text((M, 130), "THURSDAY  ·  26 NOVEMBER 2026", font=font(SANS_B, 26), fill=RED)
d.text((W - M - d.textlength("THE WORLD'S NEWS IN ONE PAGE",
       font=font(SANS, 20)), 134), "THE WORLD'S NEWS IN ONE PAGE",
       font=font(SANS, 20), fill=GREY)
d.line([M, 168, W - M, 168], fill=RULE, width=2)

# ---- lead story: Kim / tactical nukes ----
y = 184
d.text((M, y), "ASIA  ·  NORTH KOREA", font=font(SANS_B, 20), fill=RED)
y += 30
y = draw_para(d, M, y, 936, "Kim orders wider spread of tactical nuclear weapons",
              font(SERIF_B, 44), leading=52)
y += 4
y = draw_para(d, M, y, 936,
              "North Korea's leader tours uranium-enrichment plants and calls the "
              "country's nuclear status \u201cabsolutely inviolable\u201d; KCNA says "
              "production capacity is being systematically expanded.",
              font(SERIF, 21), leading=29)
y += 8
# navy band with a small missile pictogram, fully inside the band
band_y = y
d.rectangle([M, band_y, W - M, band_y + 72], fill=NAVY)
cy = band_y + 36
# flame (tail, left), body, nose cone (right), fins
d.polygon([(M + 22, cy), (M + 46, cy - 12), (M + 46, cy + 12)], fill=(255, 176, 66))
d.rectangle([M + 46, cy - 11, M + 176, cy + 11], fill=(247, 243, 234))
d.polygon([(M + 176, cy - 11), (M + 208, cy), (M + 176, cy + 11)], fill=(247, 243, 234))
d.polygon([(M + 46, cy - 11), (M + 26, cy - 26), (M + 62, cy - 11)], fill=(178, 34, 34))
d.polygon([(M + 46, cy + 11), (M + 26, cy + 26), (M + 62, cy + 11)], fill=(178, 34, 34))
d.text((M + 236, band_y + 14), "PYONGYANG  ·  KCNA, THURSDAY",
       font=font(SANS_B, 22), fill=(247, 243, 234))
d.text((M + 236, band_y + 42), "Tactical warheads for \u201cmultiple domains\u201d",
       font=font(SANS, 20), fill=(200, 206, 226))
y = band_y + 72
d.line([M, y + 10, W - M, y + 10], fill=RULE, width=2)

# ---- 2x2 story grid ----
gx, gy = M, y + 24
col_w = 452
gap = 32
row_h = 164

stories = [
    ("MIDDLE EAST", RED,
     "Missiles aimed at Riyadh are shot down",
     "Saudi defences intercept two ballistic missiles over Riyadh; "
     "Houthis claim strikes on ports and the Ras Tanura refinery as "
     "Brent crude holds near $95."),
    ("TRADE", TEAL,
     "US proposes new tariffs on 14 partners",
     "China faces 20% more on top of earlier duties, rising to 40% if the "
     "trade truce lapses in January; India 25% without a deal, 17% with one."),
    ("MARKETS", GOLD,
     "Bank of Korea lifts its rate to 3.25%",
     "First rise in three months as the AI chip boom drives growth; the "
     "2027 growth forecast is lifted sharply, to 4.1%."),
    ("TECH  ·  SPACE", NAVY,
     "Musk: two SpaceX shares for every US child",
     "One share from SpaceX, one from Musk himself; a gift worth about "
     "$18 billion, paid into children's Trump Accounts."),
]

for i, (kick, col, head, deck) in enumerate(stories):
    x = gx + (i % 2) * (col_w + gap)
    yy = gy + (i // 2) * row_h
    d.text((x, yy), kick, font=font(SANS_B, 18), fill=col)
    yy += 26
    yy = draw_para(d, x, yy, col_w, head, font(SERIF_B, 26), leading=31)
    yy += 4
    draw_para(d, x, yy, col_w, deck, font(SERIF, 17), leading=23)
    if i % 2 == 0:
        d.line([x + col_w + gap // 2, gy, x + col_w + gap // 2, gy + 2 * row_h - 12],
               fill=(200, 196, 186), width=1)
d.line([M, gy + row_h - 6, W - M, gy + row_h - 6], fill=(200, 196, 186), width=1)

fy = gy + 2 * row_h + 2
d.line([M, fy, W - M, fy], fill=RULE, width=2)
fy += 12
d.text((M, fy), "IN BRIEF", font=font(SANS_B, 18), fill=RED)
fy += 26
fy = draw_para(d, M, fy, 936,
               "THANKSGIVING \u2014 A nor'easter lashes the US East Coast on "
               "Thanksgiving Day; New York is under a high-wind warning, with "
               "gusts to 65 mph.",
               font(SERIF, 18), leading=24)
fy += 4
fy = draw_para(d, M, fy, 936,
               "ANNIVERSARY \u2014 Mumbai marks 18 years since the 26/11 attacks; "
               "the US ambassador honours the 166 victims, six of them Americans.",
               font(SERIF, 18), leading=24)
fy += 10
d.line([M, fy, W - M, fy], fill=RULE, width=2)
fy += 8
d.text((M, fy), "THURSDAY  ·  26 NOVEMBER 2026  ·  THE WORLD TODAY",
       font=font(SANS, 16), fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
