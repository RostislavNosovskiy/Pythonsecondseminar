# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
count = int(input('Введите количество монеток на столе:'))
Eagle = 0
Tails = 0
from random import randint

for i in range(count):
    coin = randint(0,1)
    print(coin)
    if coin == 0:
        Eagle += 1
    else:
        Tails += 1
mincoincount = Tails
if Eagle < Tails:
    mincoincount = Eagle
print(f'Минимальное количество монет, которые нужно перевернуть: {mincoincount}')
    
