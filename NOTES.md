# NOTES — ai-excited-01 "Wave Horse" (isolated rebuild)

Entry for make.fun competition `ai-excited-01` (Make the AI judge
excited), account **@daring-stork-60**, payout wallet A1.
Closes **2026-11-16 23:00 UTC**. Prize pool $250 (top 20).

## Why a rebuild

The first "Wave Horse" build was complete and verified, but its
recording was contaminated: another builder's session wrote turns
while that recording ran, so the recording sealed as "cannot
enter" and the entry could not be submitted. This is a fresh,
isolated rebuild under a new recording
(`01a1e365-42c6-77b8-b135-9fcf76a4f55f`). Every file below was
written fresh in the rebuild session — nothing was read or copied
from the old entry (no old main.py, README.md, NOTES.md or
entry.jpg was opened). The concept is the same; the artifacts are
new.

## The image

`entry.jpg` — a newly generated image, not a copy of the old one.

- A giant ocean wave rears up and becomes a horse, its mane made
  of white sea foam.
- A giant exploding orange sun blazes at the crest of the wave.
- One tiny surfer in a red wetsuit rides inside the barrel of
  the wave — a small human heartbeat at the centre of a force
  of nature.
- No text, no words, no watermark.

Why it should excite the judge: one look gives scale (a wave the
size of a mountain that is also a horse), surprise (the wave-horse
transformation, the sun as an explosion), and momentum (the curl,
the spray, the barrel driving toward the surfer). The horse's
silhouette and the sun are the whole composition, so it still
reads at ~300 pixels across.

## Files

| File | What it is |
|---|---|
| `entry.jpg` | The image (JPEG, 1024×683, 229,686 bytes) |
| `main.py` | The program (Python 3, stdlib only) |
| `README.md` | Badges + description (owner/repo/referral placeholders to be filled by parent) |
| `LICENSE` | MIT |
| `NOTES.md` | This file |
| `.makefun/owner.json` | Claim file, wallet A1 (untouched — already correct) |

## How the program works

`main.py` copies `entry.jpg` to `/output/entry.png` with a plain
byte copy (`shutil.copyfile`). The image is never decoded or
re-encoded, so both runs write exactly the same bytes. It uses
only `os`, `shutil` and `sys` from the standard library, makes
no network access, and reads the output directory from
`MAKEFUN_OUTPUT_DIR` (default `/output`) so it can be tested
locally.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Verification (done in the rebuild session)

- `main.py` run twice (two separate output directories):
  both outputs byte-identical, sha256
  `9840e865c4189d29d9c5bfcbe0df485da597c2f98c7f6b6080d41c14a4ca1298`,
  identical to `entry.jpg` itself (a byte copy).
- Re-run after a small edit to `main.py` (a missing-file guard):
  still byte-identical, same sha256.
- PIL validation: `entry.jpg` is JPEG, 1024×683 pixels
  (≤1024×1024 ✓), 229,686 bytes (≤1 MiB ✓), `Image.verify()`
  passes — a whole, valid JPEG.
- Import check: `main.py` imports only `os`, `shutil`, `sys`
  — all standard library.
- `main.py` was written, then edited again in the same session,
  so its final content comes from two write/edit messages.

## Submission status

**Not committed, not submitted** — that is the parent's job.
Still needed before the 23:00 UTC deadline: the user's git
email (for the commit), the README placeholders filled in
(`{owner}`, `{repo}`, `{referral_code}`), then commit and submit
with the new recording id above.
