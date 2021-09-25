'''
def myname(name):
    #this will print my name
    print('this is :',name)
    return
myname('khalid')

#required argument
def add(a,b,c): 
    return a+b+c

print(add(5, 20, 15))

#keyword argument
def add2(a,b,c): 
    return a+b+c

print(add2(a= 50, b= 21,c= 12))

#default argument
def add3(a,b,c=4): 
    return a+b+c

print(add3(5, 20)) #print(add3(5, 20, 10)) then c will take 10: not 4

#variable_length argument
def add5(*value):  #non - keyword 
    print(type(value))
    temp = 0
    for number in value:
        temp = temp + number
    return temp

print(add5(5,2,6,8,6,9,2,3))

def add6(**value):  #  keyworded
    print(type(value))
    temp = 0
    for number in value:
        temp = temp + value[number]       
    return temp

print(add6(a=5,b=2,c=6,d=8,e=6,f=9,g=2,h=3))


#recursion

def factorial(n): #factorial
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(n =int(input('input ur number : '))))

#lambda

sum = lambda a,b :a+b
print(sum(5,5))

#map function
my_list = [2,3,5,9,7,8]

def sqaure(x):
    return x**2
new_list = map(sqaure,my_list)

print(new_list)
print(list(new_list))


a,b = (map(int , input().split()))

print(type(a))
print(type(b))
print(a+b)


#filter function
my_list = [2,3,5,9,7,8,10,12]

def even(a):
    if a % 2 == 0:
        return True
    else:
        return False 

print(list(filter(even, my_list))) #even function and my_list iterable

#problem 1:

a,b,c = list(map(int , input().split()))

def greater():
    temp = 0
    if a > b:
        temp = a
    else:
        temp = b
    if temp > c:
        great = temp
    else:
        great = c
    return great

print(greater())

#problem 2: GCM

def gcd(a,b):
    if b >a:
        gcd(b,a)
    while b !=0 :
        temp =a %b
        a = b
        b = temp
    return a

a,b = map(int , input('please enter two number: ').split())
print(gcd(a,b))

#problem 3: LCM
def gcd(a,b):
    if b >a:
        gcd(b,a)
    while b !=0 :
        temp =a %b
        a = b
        b = temp
    return a
def lcm(a,b):
    return (a*b) // gcd(a,b)
a,b = map(int , input('please enter two number: ').split())
print(lcm(a, b))
'''
#problem 4: prime

# Python program to check if
# given number is prime or not
 
num = int(input('enter your number : '))
flag =  False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is a composite number")
else:
    print(num, "is a prime number")
    

'''
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)
 
greet(shout)
greet(whisper)
'''