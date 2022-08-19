import random
rz = 0
while rz < 3:
    user_number = int(input('Enter number from 1 to 10'))
    lottery_number = random.randint(0, 10)
    if user_number == lottery_number:
        print('You won!')
    else: print('You lose!')
    rz +=1
    continue


