v = int(input('PLease enter your speed:'))
t = int(input('Please enter your time:'))
s = v * (abs(t))
if v > 0 and s < 100:
    print (f'You are already completed {s} km.Keep it ip!')
elif v < 0 and s <=100:
    print(f' You are delayed for {abs(s)} km. Harry up!')
else:
    print('Congratulations! You are already finished 100 km!')
