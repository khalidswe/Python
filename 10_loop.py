#while loop
'''
n= 1
while n<=5:
    print(n)
    n=n+1

#shotokia
s = 1
temp =0

while s <=100:
    temp = temp+s
    s = s+1
print(temp)

#break statement
while n <50:
    print(n)
    if n==40:
        break
    n+=1

a = 'python'
for letter in a:
    print(letter.upper())

print(range(5))
print(list(range(5)))

print(list(range(5,20)))

for number in range(1,20):
    if number == 5: #just skip this 5
        continue
    print(number)

# same pass and break statement 

n =1
while n <10:
    print(n)
    n+=1
else :            #using else in while loop
    print('loop is over')


#p1 (marteen's book)

value = int(input())
count = 0
while count <=10:
    print(value, '*' ,count,' = ',value*count)
    count+=1

#p2 (marteen's book)

mylist=[]

for i in range(1,100):
    if i%3==0 and i%5!=0:
        mylist.append(i)
        
print(mylist)


#p3 (marteen's book)
mylist=[13,34,19,28,46,61,73,49,1,31,4,7,91,58,52,82,70,43,88,55,97,16,22,25,79,85,40,64,94,67,37]
print_list = []
for number in mylist:
    if number <50:
        print_list.append(number)
print(print_list)


#p4 (marteen's book)
mylist = [40,45,33,34,8,38,28,22,1,7,49,41,14,5,22,39,15,19,36,37,43,2,5,42,46,48,49,12,48,37,8,20,30,20,4,37,27,29,7,44,15,32,35,10,28,18,2,15,36,38]
print_list=[]
for number in mylist:
    if number  not in print_list:
        print_list.append(number)

print(print_list)

#p5 (marteen's book)
value = int(input()) 
i = 0
for i in range(value):
    print(value*'*')

#1
i =1
temp = 0

while i <=100:
    temp = temp+i
    i+=1
print(temp)

#p2
value = int(input('enter your value: '))
i=1
for i in range(value+1):
    print(i*'*')
'''
