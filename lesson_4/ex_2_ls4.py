import statistics

user_input = None
el_to_op = []

while user_input !=0:
    user_input = int(input('Enter number'))
    el_to_op.append((int(user_input)))
el_to_op = el_to_op[:-1]

# кількість введених чисел
number_of_elements = len(el_to_op)
print("Кількість введених чисел: ", number_of_elements)

# їхню суму
sumOfElements = 0
for element in el_to_op:
    sumOfElements = sumOfElements + element
print("Сума:", sumOfElements)

# #добуток
import math
i = math.prod(el_to_op)
print('Добуток', i)

# середнє арифметичне (крім завершального числа 0)
s = statistics.mean(el_to_op)
print('Середнє арифметичне',s)

# Визначити значення та порядковий номер найбільшого елемента послідовності. Якщо найбільших елементів є кілька,
# виведіть порядковий номер першого з них. Нумерація елементів починається з 1 (однини)
m = max(el_to_op)
n = el_to_op.index(m)
print('Найбільший елемент послідовності', +(m))
print('Порядковий номер найбільшого елементу',n+1)

# визначити кількість парних та непарних елементів у послідовності
r_pr = []
r_npr = []
for digit in el_to_op:
    if digit % 2 == 0:
        r_pr.append(digit)
    elif digit % 2 != 0:
        r_npr.append(digit)
r_pr.sort()
print('Парни',r_pr)
r_npr.sort()
print('Не парни',r_npr)

# Визначити значення другого за величиною елемента в цій послідовності
el_to_op.sort()
print(el_to_op[-2])

# визначте, скільки елементів цієї послідовності дорівнюють її найбільшому елементу
nb = el_to_op[-1]
count = 0
for ch_nm in el_to_op:
    if ch_nm == nb:
        count += 1
print(count, 'елементів цієї послідовності дорівнюють її найбільшому елементу, а саме числу', nb)
