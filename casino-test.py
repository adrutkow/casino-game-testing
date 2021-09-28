import random


init_money = 10000
money = init_money
bet = 100
multiplicators = [7, 2, 1, 4, 21, 0]
strings = ["3 same", "2 same", "1 diamond", "2 diamonds", "3 diamonds", "nothing"]
counter = [0, 0, 0, 0, 0, 0]
log = False


def howManyDiamonds(x):
    diamonds = 0
    for i in x:
        if i == 0:
            diamonds += 1
    return diamonds


def howManySameColor(x):
    y = []
    for i in x:
        if i > 1:
            y.append(x.count(i))
    if len(y) == 0:
        return 0
    return max(y)


def prizeMultiplicatorIndex(x):
    color = howManySameColor(x)
    diamond = howManyDiamonds(x)

    if color == 3:
        return 0
    if diamond == 1:
        return 2
    if color == 2:
        return 1
    if diamond == 2:
        return 3
    if diamond == 3:
        return 4

    return 5


for i in range(0, 100000):
    money = money - bet
    x = [random.randint(0, 8), random.randint(0, 8), random.randint(0, 8)]
    if log:
        print(x)
    i = prizeMultiplicatorIndex(x)
    if log:
        print(strings[i] + ", x" + str(multiplicators[i]))
    counter[i] += 1
    money = money + bet * multiplicators[i]
    if log:
        print(str(money) + "$")

print("================")
print("attempts =", sum(counter))
print("start money =", init_money)
print("end money =", money)
for i in range(0, len(multiplicators)):
    percent = (counter[i] / sum(counter)) * 100
    print("(x" + str(multiplicators[i]) + ")" + strings[i] + " = " + str(counter[i]) + "(" + str(percent) + "%)")
print("================")


