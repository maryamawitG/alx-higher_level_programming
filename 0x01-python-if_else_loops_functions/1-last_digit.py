#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = -ld
print("Last digit of {} is {}".format(number, ld))
if ld > 5:
    print("and is greater than 5")
elif ld == 0:
    print("and is 0")
elif (ld < 6) and (ld != 0):
    print ("and is less than 6 and not 0")
