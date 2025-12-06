sales = [
    {"day": "Mon", "rev": 200, "cost": 250},
    {"day": "Tue", "rev": 400, "cost": 300}
]
for d in sales:
    profit = d["rev"] - d["cost"]
    if profit < 0:
        label = "Loss"
    elif profit < 50:
        label = "Low Margin"
    elif profit < 200:
        label = "Healthy"
    else:
        label = "Peak"
    print(d["day"], "=>", label)

