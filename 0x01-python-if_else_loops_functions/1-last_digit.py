#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ln = -1 * int(str(number)[-1])
else:
    ln = int(str(number)[-1])
if ln > 5:
    print("Last digit of", number, "is", ln, "and is greater than 5")
elif ln == 0:
    print("Last digit of", number, "is", ln, "and is 0")
else:
    print("Last digit of", number, "is", ln, "and is less than 6 and not 0")
