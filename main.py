import itertools

COSTS = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
BENEFITS = [.05, .1, .15, .2, .17, .25, .07, .11, .13, .27, .17, .09, .23, .01, .03, .08, .12, .14, .21, .18]

shares = []
best_benefit = 0
best_combination = None

for i in range(20):
    share = {i+1: {COSTS[i]: BENEFITS[i]}}
    shares.append(share)


def accept_combination(combination: tuple) -> bool:
    total = round(sum(combination), 2)
    if total < 500:
        return True
    else:
        return False


def compare_combinations(first_cmb: float, second_cmb: float) -> float:
    if second_cmb > first_cmb:
        return second_cmb
    else:
        return first_cmb


for cmb in itertools.combinations_with_replacement(shares, 1):
    combinations = []
    total_benefit = []
    for action in cmb:
        for key in action.keys():
            combinations.append(COSTS[key-1])

    is_accepted = accept_combination(tuple(combinations))
    if is_accepted:
        for item in cmb:
            for k in item.keys():
                absolute_benefit = round((COSTS[k-1] * BENEFITS[k-1]), 2)
                total_benefit.append(absolute_benefit)
        comparison = compare_combinations(best_benefit, sum(total_benefit))
        if best_benefit < comparison:
            best_benefit = comparison
            best_combination = cmb

print(f"meilleur combinaison = {best_combination}")
