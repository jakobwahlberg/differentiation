"""
THE AXIOM — clean consolidated simulation.

A structural/relational lens on the propagation of the universe. Parameter-free:
every quantity is a relation derived from the break itself. Nothing is coded to
cycle; whatever recurs, recurs from the clauses alone.

CLAUSES
  1. A symmetry break from infinity creates a gradient. The gradient forces
     differentiation. The break is the whole; the root is its inexhaustible seat.
  2. A coherence node's range is the unspent remainder funnelled down to it:
     range(d) = 1/(d+1). Budget and range are one quantity, not two ledgers.
     Range shrinks per substrate. The root's range is the whole (1).
  3. Placement is a structural draw u ~ uniform[0,1). It succeeds iff u falls
     within the substrate's EFFECTIVE range (range minus absorbed feedback).
  4. DIFFERENTIATION IS ONE-SHOT. A node attempts until it either actualises
     exactly one child (funnels down, goes quiet, becomes STUFF) or burns
     (feedback drives its effective range to <= 0). Then it exits. It never
     differentiates again.
  5. A failed attempt duplicates the node: a silent, inert duplicate persists
     in the record. No budget spent. No new distinction made.
  6. Feedback: a failed attempt's overshoot (u - effective) recedes to the
     nearest coherent ancestor, which absorbs it. The root absorbs harmlessly
     and is never decohered.
  7. Spending = making a distinction that cannot be made again. The FIRST
     actualisation at a given depth is novel (a degree of freedom committed);
     every later actualisation at an achieved depth is duplication.
  8. Actualised nodes are STUFF. How stuff interacts is OUT OF SCOPE.

The lens hands off, exactly here, to physics.
"""
import random
from collections import Counter

def simulate(ticks, seed):
    rnd = random.Random(seed)

    class Node:
        __slots__ = ("d", "fb", "parent")
        def __init__(self, d, parent):
            self.d = d; self.fb = 0.0; self.parent = parent
        @property
        def effective(self):
            return 1.0 - self.fb if self.d == 0 else 1.0/(self.d + 1) - self.fb

    root = Node(0, None)

    stuff      = Counter()   # actualised nodes, by depth (they exit as "stuff")
    burned     = Counter()   # nodes that burned, by depth (structured residue)
    duplicates = Counter()   # inert silent duplicates, by attempted depth
    achieved   = set()       # depths at which a distinction has ever been made
    novelties  = []          # (tick, depth) of each genuinely new distinction
    active_depth_trace = []  # depth of the live differentiation front each tick

    tip = root               # the single live front; root re-seeds when a chain ends
    for t in range(ticks):
        u = rnd.random()                      # structural draw over the whole
        child_depth = tip.d + 1
        if u < tip.effective:
            # ACTUALISE: place the one child, funnel down, tip becomes stuff
            if tip.d > 0:
                stuff[tip.d] += 1
            if child_depth not in achieved:   # clause 7: novelty vs duplication
                achieved.add(child_depth)
                novelties.append((t, child_depth))
            tip = Node(child_depth, tip)       # differentiation funnels down
        else:
            # FAIL: inert duplicate persists; overshoot recedes to coherent ground
            duplicates[child_depth] += 1
            overshoot = u - max(tip.effective, 0.0)
            anc = tip
            while anc is not root and anc.effective <= 0:
                anc = anc.parent
            if anc is not root:
                anc.fb += overshoot
            # one-shot: if the tip can no longer cohere, it burns and the chain ends
            if tip is not root and tip.effective <= 0:
                burned[tip.d] += 1
                tip = root                     # the inexhaustible root re-seeds
        active_depth_trace.append(tip.d)

    return dict(stuff=stuff, burned=burned, duplicates=duplicates,
                novelties=novelties, trace=active_depth_trace)

# ---- run one clean observation ----
TICKS = 1_000_000
r = simulate(TICKS, seed=1)

S = sum(r["stuff"].values())
B = sum(r["burned"].values())
D = sum(r["duplicates"].values())
depths = sorted(set(r["stuff"]) | set(r["burned"]) | set(r["duplicates"]))

print(f"observation window: {TICKS:,} ticks\n")

print("CENSUS  (stuff : burned : inert-duplicates)")
print(f"  totals   {S:>9,} : {B:>9,} : {D:>10,}")
print(f"  ratio    {S/B:>9.2f} : {'1.00':>9} : {D/B:>10.2f}\n")

print("LAYER INVENTORY  (per depth)")
print(f"  {'depth':>5} | {'stuff':>9} | {'burned':>8} | {'duplicates':>10} | {'x prev layer':>12}")
prev = None
for d in depths:
    layer = r["stuff"][d] + r["burned"][d] + r["duplicates"][d]
    ratio = f"{prev/layer:.2f}x" if prev else "-"
    print(f"  {d:>5} | {r['stuff'][d]:>9,} | {r['burned'][d]:>8,} | {r['duplicates'][d]:>10,} | {ratio:>12}")
    prev = layer

print("\nNOVELTY  (first distinction committed at each depth)")
for t, d in r["novelties"]:
    print(f"  depth {d}: first actualised at tick {t:,}")
total_actualisations = S + r["stuff"][0] if 0 in r["stuff"] else S
# recompute cleanly: every actualisation, novel or duplicate
novel = len(r["novelties"])
# count all actualisations across trace transitions
actualisations = sum(1 for i in range(1, len(r["trace"])) if r["trace"][i] > r["trace"][i-1])
print(f"\n  novel distinctions: {novel}")
print(f"  total actualisations: {actualisations:,}")
print(f"  repetition fraction: {1 - novel/actualisations:.6%}")
last = r["novelties"][-1][0]
print(f"  last novelty at tick {last:,}; {TICKS-last:,} ticks of pure repetition since")

print("\nFRONT  (live differentiation depth)")
occ = Counter(r["trace"])
print("  occupancy:", {k: round(v/TICKS, 3) for k, v in sorted(occ.items())})
print(f"  max depth reached: {max(r['trace'])}")
print(f"  production rate: {(S+B)/TICKS:.3f} exiting nodes per tick")

# emergent front trace (first 240 ticks) for the chart
print("\nTRACE240", ",".join(map(str, r["trace"][:240])))
