print("Добро пожаловать в игру 'Быки и Коровы'! ")
print("Сделайте ход, введя 4х значное число:")
from random import randint

str_result = str(randint(1000, 9999))
num = 0

while True:
    num += 1
    print("Номер попытки=", num)
    x = str(input())
    if str(x) == str(str_result):
        print('Вы угадали')
        break
    elif len(str(x)) != 4 or not x.isdigit():
        print("Ввод не соответствует правилам игры")
        continue
    else:
        print("Увы, вы не угадали")
    y = list(str_result)
    z = list(x)
    bulls = 0
    for i in range(4):
        if z[i] == y[i]:
            bulls += 1
            z[i] = ''
            y[i] = '*'
    cows = 0
    for i in range(4):
        k = z[i]
        for c in range(4):
            if k == y[c]:
                cows += 1
                y[c] = '*'

    print("Число коров =", cows)
    print("Число быков =", bulls)

