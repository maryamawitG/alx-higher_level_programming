#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print('Negative')
elif number == 0:
    print('Zero')
else:
    print('positive')
