#Дано два цілих числа 'A' і 'В'. Виведіть усі числа від `A` до `B` включно, в порядку зростання, якщо `A < B`, або в порядку зменшення в іншому випадку.
a = int(input('Введіть число А'))
b = int(input('Введіть число В'))
i = int()

if a <=b:
    for i in range(a,b+1): print(i)
else:
    for i in reversed(range(b, a+1)):
        print(i)
