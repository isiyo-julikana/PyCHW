"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
    
"""
from math import sqrt
from random import randint
print("Петя загадывает числа...")
numbX= int(randint(1, 1000))
numbY= int(randint(1, 1000))
print("И дает подсказки...")
sum = int(numbX + numbY)
mult = -int(numbX * numbY)
print("Сумма загаданых чисел - {}, а произведение - {}".format(sum, abs(mult)))
D = sum*sum + 4*mult  
if D > 0:
    sq = sqrt(D)/2
    p = sum/2
    x = int(p-sq)
    y = int(p+sq)
print("У Кати получились числа {} и {}".format(x,y))
if (((x == numbX and y == numbY) or (y == numbX and x == numbY))):
    print("Катя угадала правильно")
else: print("Катя не угадала. Как это возможно?")


print("Загаданые числа были: {} и {}.".format(numbX, numbY))


