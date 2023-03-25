#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = -ld
print("Last digit of {} is {}".format(number, ld), end='')
if ld > 5:
    print("and is greater than 5".format(number, ld))
elif ld == 0:
    print(" and is 0".format(number, ld))
else:
    print("and is less than 6 and not 0".format(number, ld))
