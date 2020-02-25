#!/usr/bin/env python3

import random

def countdown(x, s):
    """This is a recursive function
    that counts down from a random integer to 0"""

    # base case
    if x == 0:
        return 0
    else:
        return str(x) + " " + str(countdown(x-1, s))

x = random.randint(1,25)
print("From ", x, "is:")
print(countdown(x, ''))