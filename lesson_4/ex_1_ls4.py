x = int(input('Enter km for start'))
y = int(input('Enter km for goal'))
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)