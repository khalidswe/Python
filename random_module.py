#import random

#from  random import functionname
#import random

from random import choice
l1 = [1,2,5,6,8,10,7]
print(choice(l1))

from random import  randint

otp = randint(10000,99999) # range ( a to b)
print("otp :",otp)


from random import shuffle

l2= ["apple","banana","mango"]
shuffle(l2)
print(l2)

