import csv


def combinations_with_replacement(read_file: str, write_file: str):
    """
    For each share in the list, add it to the combination while the wallet is inferior to 500.

    :param read_file: the datasets file in .csv format.
    :param write_file: the file the report will be written in.
    """
    selected_shares = []
    wallet = 0
    total_profit = 0

    sorted_shares = create_shares_from_file(read_file)

    for share in sorted_shares:
        while True:
            wallet += share[1]['price']
            if wallet <= 500:
                total_profit += ((share[1]['price'] * share[1]['profit']) / 100)
                selected_shares.append(share[0])
                continue
            else:
                wallet -= share[1]['price']
                break

    write_report(selected_shares, wallet, total_profit, write_file)


def combinations_without_replacement(read_file: str, write_file: str):
    """
        For each share in the list, add it to the combination if the wallet is inferior to 500.

        :param read_file: the datasets file in .csv format.
        :param write_file: the file the report will be written in.
        """
    selected_shares = []
    wallet = 0
    total_profit = 0

    sorted_shares = create_shares_from_file(read_file)

    for share in sorted_shares:
        wallet += share[1]['price']
        if wallet <= 500:
            total_profit += ((share[1]['price'] * share[1]['profit']) / 100)
            selected_shares.append(share[0])
        else:
            wallet -= share[1]['price']

    write_report(selected_shares, wallet, total_profit, write_file)


def create_shares_from_file(read_file: str) -> list:
    """
    Read a .csv file as a dictionary. For each row, if the column 'price' is superior to 0,
    create a new key with the 'name' column, and a second dictionary as value.
    The second dictionary has two keys: 'price' and 'profit'.

    :param read_file: the .csv file to read.
    :return: the sorted shares dictionary by 'profit' and reversed.
    """
    shares = {}

    with open(read_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                line_count += 1

            if float(row['price']) > 0:
                shares[row['name']] = {"price": float(row['price']), "profit": float(row['profit'])}

    return sorted(shares.items(), key=lambda s: (s[1]['profit'], s[1]['price']), reverse=True)


def write_report(shares: list, wallet: float, profit: float, write_file: str):
    """
    Write the report with the shares to buy, the total cost and the total profit.

    :param shares: the shares selected the best combination
    :param wallet: the total cost of the combination
    :param profit: the total profit of the combination
    :param write_file: the file to write the report in
    """
    with open(write_file, mode="w") as file:
        file.write("Shares to buy:\n")
        for share in shares:
            file.write(f"\t{share}\n")
        file.write(f"Total cost: {round(wallet, 2)}\n")
        file.write(f"Total return: {round(profit, 2)}")


if __name__ == "__main__":
    combinations_with_replacement('csv/dataset1_Python+P7.csv', 'reports/dataset1_with_replacement.txt')
    combinations_with_replacement('csv/dataset2_Python+P7.csv', 'reports/dataset2_with_replacement.txt')

    combinations_without_replacement('csv/dataset1_Python+P7.csv', 'reports/dataset1_without_replacement.txt')
    combinations_without_replacement('csv/dataset2_Python+P7.csv', 'reports/dataset2_without_replacement.txt')
