#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ln = int(str(number)[-1])
if number < 0:
    ln = ln * -1
if ln > 5:
    print("Last digit of", number, "is", ln, "and is greater than 5")
elif ln == 0:
    print("Last digit of", number, "is", ln, "and is 0")
else:
    print("Last digit of", number, "is", ln, "and is less than 6 and not 0")
