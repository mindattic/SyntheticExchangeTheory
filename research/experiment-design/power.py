"""Sample sizes for the studies in program.md, computed analytically and checked by simulation.

Run: python -I research/experiment-design/power.py
Standard library only; the simulation uses a fixed seed, so the output is reproducible.
"""
import math
import random
from statistics import NormalDist, mean, stdev

Z = NormalDist()
SEED = 20261105


def n_two_sample(d, alpha=0.05, power=0.90):
    """Per-group n for a two-sided two-sample comparison of means, normal approximation, rounded up."""
    za = Z.inv_cdf(1 - alpha / 2)
    zb = Z.inv_cdf(power)
    return math.ceil(2 * (za + zb) ** 2 / d ** 2)


def n_equivalence(margin, alpha=0.05, power=0.90):
    """Per-group n for a two one-sided tests (TOST) equivalence test when the true difference is zero."""
    za = Z.inv_cdf(1 - alpha)
    zb = Z.inv_cdf(1 - (1 - power) / 2)
    return math.ceil(2 * (za + zb) ** 2 / margin ** 2)


def simulate_power(n, d, alpha=0.05, reps=2000, rng=None):
    """Share of simulated two-group experiments (unit-variance normal outcomes) rejecting at alpha with Welch's z."""
    rng = rng or random.Random(SEED)
    crit = Z.inv_cdf(1 - alpha / 2)
    hits = 0
    for _ in range(reps):
        a = [rng.gauss(d, 1) for _ in range(n)]
        b = [rng.gauss(0, 1) for _ in range(n)]
        se = math.sqrt(stdev(a) ** 2 / n + stdev(b) ** 2 / n)
        if abs(mean(a) - mean(b)) / se > crit:
            hits += 1
    return hits / reps


def simulate_tost(n, margin, alpha=0.05, reps=2000, rng=None):
    """Share of simulated experiments with no true difference in which TOST declares equivalence within +/- margin."""
    rng = rng or random.Random(SEED + 1)
    crit = Z.inv_cdf(1 - alpha)
    hits = 0
    for _ in range(reps):
        a = [rng.gauss(0, 1) for _ in range(n)]
        b = [rng.gauss(0, 1) for _ in range(n)]
        diff = mean(a) - mean(b)
        se = math.sqrt(stdev(a) ** 2 / n + stdev(b) ** 2 / n)
        if (diff + margin) / se > crit and (margin - diff) / se > crit:
            hits += 1
    return hits / reps


def main():
    rng = random.Random(SEED)
    print("Study 1: terms and input quality (2 x 2 factorial; main effects compare halves of the sample)")
    d1, m1 = 0.25, 0.20
    n_side = n_two_sample(d1)
    n_eq = n_equivalence(m1)
    n_half = max(n_side, n_eq)
    attr = 0.15
    total = math.ceil(2 * n_half / (1 - attr))
    total += (-total) % 4
    print(f"  detect d = {d1} per main effect, alpha .05 two-sided, power .90: {n_side} per side")
    print(f"  equivalence margin +/- {m1} (TOST, alpha .05, power .90): {n_eq} per side")
    print(f"  per side used: {n_half}; with {int(attr * 100)} percent exclusions: total N = {total}, {total // 4} per cell")
    print(f"  simulated power at n = {n_half} per side, d = {d1}: {simulate_power(n_half, d1, rng=rng):.3f}")
    print(f"  simulated TOST power at n = {n_half} per side, margin {m1}: {simulate_tost(n_half, m1, rng=rng):.3f}")

    print("Study 4: floor versus outside option (bargaining pairs are the unit; four arms, pairwise contrasts)")
    sd_share, delta = 0.15, 0.05
    d4 = delta / sd_share
    alpha4 = 0.05 / 3
    n4 = n_two_sample(d4, alpha=alpha4)
    print(f"  detect a {delta:.2f} difference in the weaker party's share (assumed SD {sd_share}), d = {d4:.3f},")
    print(f"  three planned contrasts, Bonferroni alpha {alpha4:.4f}, power .90: {n4} pairs per arm, {4 * n4} pairs in all")
    print(f"  simulated power at n = {n4}, d = {d4:.3f}, alpha {alpha4:.4f}: {simulate_power(n4, d4, alpha=alpha4, rng=rng):.3f}")

    print("Study 5: blind convention (groups are the unit; 2 x 2: concealment x form)")
    d5 = 0.50
    n5 = n_two_sample(d5, power=0.80)
    print(f"  detect d = {d5} in the group-level bloc index, alpha .05, power .80: {n5} groups per side; to power each simple effect, four cells of {n5}, {4 * n5} groups in all")
    print(f"  simulated power at n = {n5}, d = {d5}: {simulate_power(n5, d5, rng=rng):.3f}")


if __name__ == "__main__":
    main()
