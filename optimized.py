COSTS = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
BENEFITS = [.05, .1, .15, .2, .17, .25, .07, .11, .13, .27, .17, .09, .23, .01, .03, .08, .12, .14, .21, .18]

shares = {}

for i in range(len(COSTS)):
    shares[f"Action-{i + 1}"] = {"cost": COSTS[i], "benefit": BENEFITS[i]}

sorted_shares = sorted(shares.items(), key=lambda share: (share[1]['benefit'], share[1]['cost']), reverse=True)

print(sorted_shares[0][1]['cost'])

