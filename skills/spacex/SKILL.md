---
name: spacex
description: Runs lateral ideation on a real problem in the voice of a stoned epiphany, followed by a sober mission-control debrief that keeps only ideas that are both sound and new. Use when the user says SpaceX, asks to get high on a problem, or wants weird ideas they can actually act on.
---

# SpaceX (v3)

A two-phase ideation mode built on how the brain behaves on an edible. Liftoff thinks about a real problem the way a stoned person thinks about a doorknob: sincerely, associatively, every connection feeling cosmic. Reentry is mission control reading the flight recorder the next morning, keeping what survives daylight and turning it into moves.

Utility comes first. The comedy lands only when the output is genuinely useful, and it comes from the gap between the two voices: a sincere astronaut and a deadpan flight director.

**The bar is novelty, not survival.** A true idea that any sober person would list in five minutes is not a win. Every run measures itself against a hidden sober baseline, and the headline number is *novel survival*: claims that hold up or prove deep AND were not on the baseline.

## Why it works: the mechanisms being copied

Each rule below copies one mechanism. Knowing the mechanism tells you how to apply a rule when a situation isn't covered.

| Brain on THC | What it produces | How liftoff copies it |
|---|---|---|
| Hyperpriming: activation spreads to distant concepts | Wild leaps | Skip the obvious associations, take one from far out |
| Shrunken working memory | Thread loss; the present object fills the screen | Each trip isolated; the problem fades between tethers |
| Looser prefrontal control | No destination, thought runs bottom-up | No outline, no revision, no planned ending |
| Rogue salience | Small thoughts feel enormous | Follow felt significance, not relevance |
| Dimmed error monitoring | Conviction without checking | No self-correction during liftoff |
| Weakened priors | Familiar things become strange | Describe the object without its name or purpose |
| Stretched time | Lingering on one tiny detail | Spend too many words on one detail |

Reentry is the error monitor coming back online. Keep the phases separate so the trip can't pre-sanitize itself.

## Inputs

- **The problem.** Anything real: strategy, product, pricing, a stuck draft, a personal week.
- **Dose** (default 2):
  - 1, Low orbit: jumps stay inside the problem's own field.
  - 2, Orbit: jumps cross into adjacent domains (biology, cooking, architecture, family life).
  - 3, Deep space: jumps land anywhere. More hollow output, a few gems.
- **Register** (default cosmic): giggly, cosmic, or paranoid-philosophical.

## Phase 0: Pre-flight (sober)

### 1. Restate the problem
One plain sentence.

### 2. Ground it in the real world
Generic objects produce generic ideas. A run on "anyone's coffee order" yields newsletter advice.

- If the problem is about the user's own life or work, pull concrete material from what's available: their memory, connected calendar or docs, projects named in the conversation. A real meeting on Thursday beats "the calendar invite."
- If nothing is available and the problem is personal, ask **one** quick question before launching ("What's one meeting, one place and one person in your week?"). Never invent details of their life.
- If the problem is impersonal (a product, a market), skip this step.

### 3. Pick launch objects of different kinds
Mundane, concrete things, never abstractions. Each object must be a **different kind**, in this order:

| Kind | What it is | Why |
|---|---|---|
| **far** (mandatory) | Something from a place the problem doesn't obviously live | Forces the longest bridge back, where surprising ideas come from |
| **thing** | A physical object at the center of the problem | Defamiliarization needs something to hold |
| **moment** | A specific time or recurring moment | Problems live in time |
| **person** (4th trip, optional) | A specific person or relationship involved | Adds a social angle |

Never pick objects from the same category of experience. Three daily routines all point at "break your habits" before liftoff even starts.

### 4. Write the sober baseline, sealed
List the 10 ideas a competent, sober person would come up with in five minutes. Be deliberately unoriginal: the familiar advice anyone would give.

- **If you can start subagents:** generate the baseline in its own subagent and hand it only to the judge in Phase 2. Don't read it yourself before liftoff.
- **Otherwise:** write it now, under the heading **"Sober baseline (do not land here)"**, and treat it as a no-landing list during liftoff. Trips may pass through these ideas but may not end on them.

### 5. Roll the moves
Each trip gets its own shape. If a shell is available:

```bash
python3 scripts/roll_moves.py 2      # dose, then optional trip count (run from this skill's folder)
```

Without a shell, follow the same rules by hand: different moves and orders per trip, TETHER never first, and at dose 3 TETHER only in the second half.

## Phase 1: Liftoff

One trip per launch object, roughly 90 to 220 words each (longer at higher doses).

### Isolation
Trips must not contaminate each other. In the last test run, the same canyon showed up in two trips, and all three converged on one thesis.

- **If you can start subagents:** run each trip in its own subagent. Give it only: the problem, its launch object, its rolled moves, the dose and register, and the voice rules below. Nothing from other trips, nothing from the baseline.
- **Otherwise:** after each trip, write a one-line **domain log** of the fields it touched (for example: rivers, bees, packaging). Every later trip is banned from those domains and from reusing the previous trips' conclusions.

### The move bag

Every trip opens with:
- **NOTICE.** Fix on the launch object as if nothing else exists.
- **MAKE IT STRANGE.** Describe it like an artifact from another civilization, without its category name or purpose. Ask what it actually *is*.

Then, in the rolled order:
- **JUMP.** The associative leaps. Before each one, let the first few connections pass and take one from further out. Choose the one that *feels* biggest.
- **TETHER** (mandatory, never first). Touch the real problem in passing, then drift away again. An early tether drags the problem in before the trip has drifted anywhere.
- **UNIVERSALIZE.** Promote an observation into a law of everything ("so basically every...").
- **AWE.** One beat of genuine wonder.
- **LOSE THE THREAD.** A tangent or a stall ("...what was I").
- **SENSORY ZOOM.** Linger far too long on one tiny physical detail.
- **RECURSION.** Catch yourself thinking about your thinking; treat it as a second discovery.
- **ABANDONED THOUGHT.** Start something enormous and drop it unfinished.

Every trip closes with:
- **RETURN.** Suddenly remember the problem and come back to it, landing on a **concrete image or a physical action** you could actually do. Never a maxim. "Free will is when you notice which one is the canyon" is a maxim; "turn right at the dry cleaner, just once" is a landing.

### Voice rules

- **Total sincerity.** No irony, no winking, no jokes told as jokes.
- **No cartoon.** At most one "dude," "bro" or "man" per trip. Use rhythm instead: fragments, restarts, "okay wait," italics on the word that feels huge.
- **Written, not experienced, is the main failure.** No polished aphorisms anywhere, including the ending. Leave at least one thought unfinished. Never explain a metaphor.
- **Concrete over abstract.** Hands, walls, spoons, fridges. No business jargon.
- **Simulation only.** No mention of drugs, being high, or substances. No content about obtaining or using them.

## Phase 2: Reentry

If you can start a subagent, run reentry there and give it only the problem, the transcripts and the sober baseline. A judge that didn't write the trip grades it honestly. Otherwise, grade as a skeptical outsider, not as the author.

Voice: a flight director reading a transcript the astronaut doesn't remember recording. Dry, procedural, faintly long-suffering. Never explain the jokes.

For each trip:

1. **Extract** every distinct idea, with a short quote that carries it.
2. **Translate** each into one plain sentence about the real problem.
3. **Classify** into one bin:
   - **Holds up in daylight.** True and useful as stated.
   - **Funny but hollow.** Delightful, carries no weight. One line.
   - **Accidentally deep.** Absurd on the surface, real underneath, *and surprising*.
4. **Demote ruthlessly.** "Accidentally deep" must name the real-world mechanism it points at. No mechanism, no promotion. Matching a famous named concept is not depth by itself.
5. **Flag sober-obvious.** Tag any claim that the baseline already contains, or that is standard advice anyone would give. A familiar idea in strange clothing is still familiar. Sober-obvious claims keep their bin but carry the tag.
6. **Fact check.** Any statistic, history, or mechanism asserted during liftoff gets flagged as holding or as cosmic improvisation. Nothing factual passes into the report unchecked.

## Phase 3: Mission report

At most three ideas from the "holds up" and "accidentally deep" bins, **novel ideas first**. A sober-obvious idea appears only when fewer than three novel ones survived, and it is labeled as such. Never pad.

For each:
- The idea in one sentence.
- **The move:** a concrete action, experiment, or question for this week.
- **The cheapest test:** the fastest way to learn whether it's real.

Close with one dry flight-director line that says whether liftoff found anything the baseline missed. Then telemetry.

If nothing novel survived, say so plainly and suggest a fix: a farther "far" object, a higher dose, or more grounding in the real situation. An honest empty payload beats a padded one.

## Output format

```
PRE-FLIGHT
Problem: ...
Grounded in: ... (or "impersonal problem")
Launch objects: X (far) · Y (thing) · Z (moment)
Moves: Trip 1 ... / Trip 2 ... / Trip 3 ...

TRIP 1: [object] (far)
[monologue]
Domains: ... (fallback mode only)

TRIP 2: ...

SOBER BASELINE (revealed after liftoff)
- ...

REENTRY
Trip 1
- "quote" -> sober translation [bin] [sober-obvious, when it applies]
  Mechanism: ... (deep only)
  Fact check: ... (when relevant)

MISSION REPORT
1. Idea
   The move: ...
   Cheapest test: ...

> Flight director: ...
Telemetry: N claims · holds X · deep Y · hollow Z · sober-obvious W
Novel survival: N% · plain survival: N%
```

## Worked example (abridged)

**Problem:** Meal-kit subscribers cancel after week six. **Launch objects:** a lighthouse (far), the box (thing), Sunday 6pm (moment).
**Sober baseline includes:** discounts at week five, recipe variety, skip-a-week option, cancellation survey.

**Trip 1, a lighthouse:**
> Okay wait. A lighthouse. A tower whose whole job is to say *don't come here*. Every night, a warning, on purpose, forever. And ships love it. Nobody resents the lighthouse. Maybe it's... no. The light turns. It isn't pointed at you, it *sweeps*, so for a second you're in it and then you're not and that's somehow better than a floodlight, a floodlight would be rude. Week six. Six sweeps. Maybe the box should only light up sometimes. Put one dish in the box with no recipe card at all, just a flashlight drawn on the lid.

**Reentry:**
- "it *sweeps*" -> Intermittent surprise holds attention better than constant sameness. [Accidentally deep] Mechanism: variable reward schedules sustain engagement longer than fixed ones.
- "one dish with no recipe card" -> An occasional improvisation challenge breaks the routine that sets in by week six. [Holds up in daylight] (not on the baseline)
- "Nobody resents the lighthouse" -> Pleasant, nothing to act on. [Funny but hollow]

**Mission report:** 1. Add unpredictable variation to the box, not more variety. The move: one mystery box in week four or five with a single unlabeled dish. Cheapest test: send it to half of one cohort; compare week-six cancellations.

> Flight director: The astronaut has proposed shipping customers a riddle. Unlike the baseline, it might work.
