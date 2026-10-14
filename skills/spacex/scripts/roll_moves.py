#!/usr/bin/env python3
"""Roll the move order for each SpaceX liftoff trip.

Usage: python3 roll_moves.py [dose] [trips]
  dose   1, 2 or 3 (default 2)
  trips  number of trips (default 3)

Rules (from SKILL.md, Phase 0 step 5):
  - Every trip opens with NOTICE, MAKE IT STRANGE and closes with RETURN.
  - Middle moves are drawn from the bag; JUMP and TETHER are always present.
  - TETHER is never the first middle move. At dose 3 it sits in the second half.
  - No two trips share the same middle sequence.
"""
import random
import sys

OPEN = ["NOTICE", "MAKE IT STRANGE"]
CLOSE = ["RETURN"]
OPTIONAL = ["UNIVERSALIZE", "AWE", "LOSE THE THREAD", "SENSORY ZOOM",
            "RECURSION", "ABANDONED THOUGHT"]
# Higher doses get more jumps and more extra moves.
JUMPS = {1: 1, 2: 2, 3: 3}
EXTRAS = {1: (2, 3), 2: (3, 4), 3: (4, 5)}


def roll_trip(dose, rng):
    middle = ["JUMP"] * JUMPS[dose] + rng.sample(OPTIONAL, rng.randint(*EXTRAS[dose]))
    rng.shuffle(middle)
    n = len(middle) + 1  # slots once TETHER is inserted
    lo = (n + 1) // 2 if dose == 3 else 1
    middle.insert(rng.randint(lo, n - 1), "TETHER")
    return middle


def main(argv):
    dose = int(argv[1]) if len(argv) > 1 else 2
    trips = int(argv[2]) if len(argv) > 2 else 3
    if dose not in JUMPS or trips < 1:
        sys.exit("usage: roll_moves.py [dose 1-3] [trips >= 1]")
    rng = random.SystemRandom()
    seen = set()
    for t in range(1, trips + 1):
        for _ in range(100):
            middle = roll_trip(dose, rng)
            if tuple(middle) not in seen:
                break
        seen.add(tuple(middle))
        print(f"Trip {t}: " + " -> ".join(OPEN + middle + CLOSE))


if __name__ == "__main__":
    main(sys.argv)
