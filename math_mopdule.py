import math

print(math.factorial(5))

import math
print(math.ceil(2.3))  #ceil take upper value and make integer value

print(math.floor(2.3)) #floor take down value and make it integer value
print(math.sqrt(100))


def rec(a):
    if a == 1:
        return 1
    else:
        return a + rec(a -1)

print(rec(10))

from random import choice
captcha = ["dawhbD","wdadd4a","awdabh5","awd78da"]
print(choice(captcha))