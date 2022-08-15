x = float(input('Enter number X'))
x = (abs(x))
spisok = list(range( 10, 101, 10 ))
if x in spisok:
     print('Это число есть в списке')
else: print('Этого числа нет в списке')