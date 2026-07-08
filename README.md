# differentiation

A single rule, run as a simulation. No tunable parameters.

## The rule

Start with a whole. A front tries to divide off a piece. If the piece coheres, it becomes the new ground and the process continues inside it. If it doesn't, it leaves a persistent trace and the front recedes to the nearest place that still coheres. Coherence range shrinks with depth. Repeat.

That is the entire model.

## What it produces

None of this is put in by hand. It falls out of the rule.

- Layered, nested structure, with a natural ceiling on depth
- A first layer that cannot fail (contestation requires prior structure)
- Continuous production that runs until nothing new is left to divide, then resets and begins again
- A specific distribution of structure across layers: Poisson, with per-layer surprisal ~ ln(d!)
- A closed form for the process: p(d) = e^(1/(d+1)) − 1
- A conserved quantity: exactly one actualization per node, at every depth

## What holds up and what doesn't

- A number matching the observed dark-matter to ordinary-matter ratio is consistent with chance. It deflates under a null test.
- The "boundary contains the whole structure" property (holography-like) is generic. A plain random walk has it too.
- The specific layer distribution is particular to this rule and survives testing.

## Run it

```
python axiom.py
```

Python 3, standard library only. No dependencies. Runs in seconds. Prints the census, the closed-form checks, and the layer distribution.

## Files

- `axiom.py` — the simulation, self-contained and commented

## Status

A structural lens, unfalsifiable by design. Not a physics claim. Stated as what it does.