import itertools
from time import time
from datetime import timedelta


def timer(function):
    def new_function(*args, **kwargs):
        start_time = int(round(time() * 1000))
        try:
            return function(*args, **kwargs)
        finally:
            elapsed_time = int(round(time() * 1000)) - start_time
            convert_milliseconds = timedelta(milliseconds=elapsed_time)
            print(f"Temps d'exécution: {convert_milliseconds}")
    return new_function


COSTS = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
BENEFITS = [.05, .1, .15, .2, .17, .25, .07, .11, .13, .27, .17, .09, .23, .01, .03, .08, .12, .14, .21, .18]

shares = []

for i in range(20):
    share = {i+1: {COSTS[i]: BENEFITS[i]}}
    shares.append(share)


def accept_combination(combination: tuple) -> bool:
    total = round(sum(combination), 2)
    if total <= 500:
        return True
    else:
        return False


def compare_combinations(first_cmb: float, second_cmb: float) -> float:
    if second_cmb > first_cmb:
        return second_cmb
    else:
        return first_cmb

    # return second_cmb if second_cmb > first_cmb else first_cmb


@timer
def main(force: int):
    best_benefit = 0
    best_combination = None

    for cmb in itertools.combinations_with_replacement(shares, force):
        combinations = []
        total_benefit = []

        for share_dict in cmb:
            for key in share_dict.keys():
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
    return best_combination, round(best_benefit, 2)


if __name__ == "__main__":
    for i in range(1, 13):
        final_result = main(i)
        print(f"Force {i}: meilleur combinaison = {final_result} \n")
