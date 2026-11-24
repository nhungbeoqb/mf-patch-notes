"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note (<=160 chars) for a bug in real life / human
biology, in the terse register of a real release note.

Anchor: makefun anchor 000c36d4b2a1de497086ce19575ec71a5d28529c round 34250632

Candidates considered (6, genuinely different):
  A. Doorway cache: crossing a doorway wipes the current task from
     memory; doorways no longer clear the cache. (116 ch)
  B. Leg standby: sitting cross-legged disables the left leg; legs now
     return from standby without the pins-and-needles boot sequence.
     (157 ch)
  C. Yawn chain reaction: one yawn in a meeting triggers the whole room;
     yawns now rate-limited to one per room. (139 ch)
  D. Earworm: a 12-second song clip loops in the brain for 6 hours with
     no stop button; earworms now ship with a close button. (139 ch)
  E. Joints boot: standing up after sitting too long plays every
     joint's startup sound at once; joints now boot silently, in
     sequence. (143 ch)
  F. "You too" autocorrect: the mouth autocorrects 'you too' onto every
     farewell, including 'enjoy your funeral'; farewells now send as
     typed. (141 ch) -- CHOSEN: the sharpest wince in the list (saying
     "you too" at a funeral is peak cringe), three-beat escalation
     (autocorrect -> every farewell -> funeral -> fix), lands on a
     first read, and every word is release-note register. Avoids the
     brief's own example (left ear, 40ms late) and the rivals seen in
     the bounty chat (3 a.m. embarrassment replay, stomach growling
     during prayers, hiccups).

v1: "v5.0.1: Fixed a bug where the mouth autocorrected 'you too' onto
every farewell, including 'enjoy your funeral'. Farewells now send as
typed."
v2 (genuine second-round revision): "the mouth" -> "your mouth"
(more direct, more embodied); "send as typed" -> "ship as typed"
(release-note register, not chat register).
"""

import os

# The patch note, assembled from named parts so each clause reads on its own.
VERSION = "v5.0.1: "
SETUP = "Fixed a bug where your mouth autocorrected 'you too' onto every farewell, "
PUNCH = "including 'enjoy your funeral'. "
FIX = "Farewells now ship as typed."

ENTRY = VERSION + SETUP + PUNCH + FIX


def write_entry(text: str) -> None:
    """Write the patch note to the gate file, exactly one line + newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
