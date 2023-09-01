"""
На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и 
той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""
def getNumber ():
    while True:
        getNumber = input('Введите количество моенток: ')
        if getNumber.isdigit() : return getNumber
n = int(getNumber())
if n == 0:
    print("Монет нет, делать нечего.")
else:
    heads = 0
    tails = 0
    x = 0
    from random import randint
    for i in range(0, n):
        x = randint(0,1)
        if x == 0:
            heads = heads + 1
        else:
            tails = tails + 1

    print("У нас {} монет, из них {} лежат орлом вверх, остальные {} решкой вверх.".format(n, heads, tails))

    if heads > tails:
        print("Минимальное количество монет, которые нужно перевернуть {}".format(tails))
    else: 
        print("Минимальное количество монет, которые нужно перевернуть {}".format(heads))