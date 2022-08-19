x1 = int(input(print('Введіть координати x1')))
y1 = int(input(print('Введіть координати y1')))
x2 = int(input(print('Введіть координати x2')))
y2 = int(input(print('Введіть координати y2')))
if (abs(x1-x2)==1 and abs(y1-y2)==2) or (abs(x1-x2)==2 and abs(y1-y2)==1):
    print('Yes')
else:
    print('No')