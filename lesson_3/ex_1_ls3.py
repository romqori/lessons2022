# Користувач вводить трицифрове число. Знайдіть суму його цифр

num = int(input("Введіть число: "))
sum = 0
if len(str(num)) !=3:
    print('Введіть 3х значну кількість')
elif len(str(num)) ==3:
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    print("Сума цифр числа дорівнює: ", sum)