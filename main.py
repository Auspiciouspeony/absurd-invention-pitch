# One-sentence absurd invention pitch for make.fun's
# "One-Sentence Absurd Invention Pitch" bounty
# (program/v1, Python 3.13, standard library only, no network).
# Writes one fixed sentence to /output/entry.txt. The gate takes UTF-8
# text of 1 to 220 characters that is not only whitespace, so the file
# holds exactly the sentence: no trailing newline, no extra words.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The sentence is fixed and deterministic: the same bytes on every run.
#
# v2 (iteration round 2 — final) — tightened from v1 against the
# judge's brief (funny from the invention itself, clever fix, original,
# tight, in that order):
# - "charging cable" -> "phone cable": the everyday object everyone
#   reaches for, one word shorter.
# - "overnight" -> "while you sleep": grounds the scene (you wake to a
#   cable that has been busy all night) and keeps the yoga mechanism.
# - "charges you for the class" -> "bills you for the class": punchier
#   verb, and the bill/charge pun lands the joke on the last words.
# Rejected in playtest: a Wi-Fi router on tiny legs that follows you
# room to room (vivid, but a robot-vacuum joke at heart, and "watch
# you ignore it in person" is a second beat that clutters); a doorbell
# that sells salespeople a timeshare (clean, but doorstep salespeople
# are not a daily annoyance for most); a toothpaste tube that files
# for retirement (the retirement is personality bolted onto the airbag
# mechanism, not the fix itself); a washing-machine sock hostage
# (funny, but sock-loss is the most reheated absurd-invention trope,
# and the sponsor's own example is a sock).

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "A phone cable that untangles itself by doing yoga while you sleep, "
    "then bills you for the class in battery percentage."
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8")
    # The grader collects outputs as another user: leave it readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
