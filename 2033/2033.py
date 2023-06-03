n = 6
amount = []
valuable = []
hot = []

for i in range(6):
    name = input()
    device = input()
    price = int(input())
    if device not in hot:
        amount.append(1)
        hot.append(device)
        valuable.append(price)
    else:
        amount[hot.index(device)] += 1
        if valuable[hot.index(device)] > price:
            valuable[hot.index(device)] = price

if amount.count(max(amount)) == 1:
    print(hot[amount.index(max(amount))])
else:
    hottest = []
    gold = []
    for i in range(len(amount)):
        if amount[i] == max(amount):
            hottest.append(hot[i])
            gold.append(valuable[i])
    print(hottest[gold.index(min(gold))])
