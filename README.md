# differentiation

A single rule, run as a simulation. No tunable parameters.

## Scope

This models differentiation only: how an undivided whole resolves into layered structure. It stops where interaction begins. Once a piece is actualized it is left alone. What actualized pieces do to each other is not part of this. The axiom produces structure and says nothing about how that structure then behaves.

## The rule

Start with a whole. A front tries to divide off a piece.

- Coherence range at depth d is 1/(d+1), the whole divided by lineage size. It shrinks with depth.
- A placement is a structural draw, uniform on [0,1).
- If the draw falls within range, the piece coheres: it becomes the new ground and the front continues inside it.
- If it falls outside, the attempt fails to propagate: it leaves a persistent trace and tries again from the same place. No budget is spent. Each failed attempt narrows what that node can still reach, until it can reach nothing and goes quiet.
- The root is the whole. Its range is 1. It never fails.

No node acts on any other node. There is no feedback between actualized pieces, because that would be interaction, which is out of scope. Each node only resolves itself.

That is the entire model.

## What it produces

None of this is put in by hand. It falls out of the rule.

- Layered, nested structure, with a natural ceiling on depth
- A first layer that cannot fail (from the root, nothing misses; contestation requires prior structure)
- A closed form for the process: p(d) = e^(1/(d+1)) − 1, the probability a fresh node at depth d coheres onward before going quiet. Matches the simulation to three decimals.
- A distribution of structure across layers that is Poisson-shaped: per-layer surprisal tracks ln((d−2)!). Reaching depth d takes d independent coherences.
- Continuous production that runs until nothing new is left to reach, then repeats. Novelty is spent early; the rest is repetition.

## Run it

```
python axiom.py
```

Python 3, standard library only. No dependencies. Runs in seconds. Prints the layered structure, the closed-form check, the layer distribution, and the reset behavior.

## Files

- `axiom.py` — the simulation, self-contained and commented

## Status

A structural lens, unfalsifiable by design. Not a physics claim. It produces layered structure and stops where interaction begins. Stated as what it does.