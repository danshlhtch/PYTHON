'''
print('Введите ваше  ниже в строке:')
name = input('')
weather = 'облачно'
age = 23
money = 2123.4


print( f'Привет, {name}, сейчас на улице {weather}')
print(f'У вас на счету {money}$' )
'''

# Выбор марки автомбиля

print('Введите марку автомобиля:')
name = input()
print('Введите молель автомобиля:')
model = input()
print('Введите год выпуска авто:')
age = input()
print('Введите рассчитываемую стоимость в $:')
price = float(input())
if price < 4000:
    print('По данный сайта ничего не надйдено')
else:
    print(f'По вашему запросу "{name} {model} {age} года" было найдено 24 автомобиля')
input()

# Игра угадай число
'''import random

print('Япредлагаю сыграть в игру угадай число')
rand = random.randint(1, 5)
numb = input('Введите любое число от 1 до 5: ')
if numb == rand:
    print('Поздравляю, вы выиграли!')
else:
    print(f'К сожалею вы проигали, программа загадала число: {rand}')
'''
'''
# Калькулятор
import numexpr

expr = input('Введите любое математическое выражение: ')
result = numexpr.evaluate(expr)
print(f'Ваш реультат равен: {result}')
'''