import itertools
from time import time
from datetime import timedelta
import csv


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


def create_shares_from_file(read_file: str) -> list:
    shares = []

    with open(read_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        line_count = 0

        for row in csv_reader:
            shares_dict = {}
            if line_count == 0:
                line_count += 1

            if float(row['price']) > 0:
                shares_dict[row['name']] = {float(row['price']): float(row['profit'])}
                shares.append(shares_dict)

    return shares


def accept_combination(combination: tuple) -> bool:
    total = round(sum(combination), 2)
    if total <= 500:
        return True
    else:
        return False


def compare_combinations(first_cmb: float, second_cmb: float) -> float:
    return second_cmb if second_cmb > first_cmb else first_cmb


@timer
def main(force: int, read_file: str):
    best_benefit = 0
    best_combination = None

    shares = create_shares_from_file(read_file)

    for cmb in itertools.combinations_with_replacement(shares, force):
        combinations = []
        total_benefit = []

        for share_dict in cmb:
            for value in share_dict.values():
                for price in value.keys():
                    combinations.append(price)

        is_accepted = accept_combination(tuple(combinations))
        if is_accepted:
            for item in cmb:
                for v in item.values():
                    for price, benefit in v.items():
                        absolute_benefit = round((price * benefit)/100, 2)
                        total_benefit.append(absolute_benefit)
            comparison = compare_combinations(best_benefit, sum(total_benefit))
            if best_benefit < comparison:
                best_benefit = comparison
                best_combination = cmb

    return best_combination, f"{round(best_benefit, 2)}€"


if __name__ == "__main__":
    for i in range(1, 10):
        with open("reports/bruteforce_report.txt", mode='r+') as file:
            if f"Force {i}" not in str(file.read()):
                print(f"Force {i} calculating...")
                final_result = main(i, 'csv/bruteforce.csv')
                file.write(f"Force {i}: meilleur combinaison = {final_result} \n")
