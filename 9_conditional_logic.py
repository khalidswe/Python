'''
value = int(input())

if value < 10:
    print('%d is smaller than 10'%value) #indentation must (4 space / 1 tab)
elif value == 10:
    print('%d  is equal to 10'%value)
else:
    print('%d is bigger than 10'%value)
'''

'''
value2 = int(input())
if value2 < 20:
    if value2 % 2 == 0:
        print('yes,less')
    else:
        print('no,less')
elif value2 == 20:
    print('%d  is equal to 20'%value2)
elif value2 > 20:
    if value2 % 3 == 0:
        print('yes,greater')
    else:
        print('no,greater')
'''
'''
#p1 : (mateen's book)

value3 = int(input())

if value3 % 3 == 0 and value3 % 5 == 0:
    print('yes')
else:
    print('no')

#p2 : (mateen's book)

value3 = int(input())

if value3 > 0:
    print('positive')
elif value3 == 0:
    print('zero')
else:
    print('negative')


#p3 : (mateen's book)

value3 = int(input())

if value3 % 2 == 0:
    print('even')
else:
    print('odd')


#p4 : (mateen's book)
print('please input character value')
value3 = input()

if value3 >= 'A' and value3 <= 'Z':
    print('uppper case')
elif value3 >= 'a' and value3 <= 'z': 
    print('lower case')
else:
    print('please check your input')


#p5 : (mateen's book)
print('please input character value')
value3 = input()

if value3 >= 'a' and value3 <= 'z' or value3 >= 'A' and value3 <= 'Z':
    if value3 in 'aeiouAEIOU':
        print('vowel')
    elif value3 not in 'aeiouAEIOU': 
        print('consonent')
else:
    print('please check your input')

'''
#p6 : (mateen's book)
print('please input your value')
bill = int(input())

b = bill
temp = bill//1000
print(temp,'  1000 takas note')
if temp > 0:
    bill = bill%1000
    b = bill
else:
    bill = b
temp = bill//500
print(temp,'  500 taka note')
if temp>0:
    bill = bill%500
    b = bill
else:
    bill = b
temp = bill//200
print(temp,'  200 taka note')
if temp > 0:
    bill = bill%200
    b = bill
else:
    bill = b
temp = bill//100
print(temp,'  100 taka note')
if temp >0:
    bill = bill%100
    b = bill
else:
    bill =b
temp = bill//50
print(temp,'  50 taka note')
if temp >0:
    bill = bill%50
    b = bill
else:
    bill =b

temp = bill//20
print(temp,'  20 taka note')
if temp >0:
    bill = bill%20
    b = bill
else:
    bill =b

temp = bill//10
print(temp,'  10 taka note')
if temp >0:
    bill = bill%10
    b = bill
else:
    bill =b

temp = bill//5
print(temp,'  5 taka note')
if temp >0:
    bill = bill%5
    b = bill
else:
    bill =b

temp = bill//2
print(temp,'  2 taka note')
if temp >0:
    bill = bill%2
    b = bill
else:
    bill =b

print(bill,'  1 taka note')
