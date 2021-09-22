c = "Bangladesh is my 'motherland' , i love her very much." # single cott must be in double cott
print(c)

d = "Bangladesh is my \"motherland\" , i love her very much." #for double cott
print(d)


print('\\') # 1 backslash print

# index
a='bangla'
print(a[2])

print(a[1:4]) # access 4 index and print 1 to 3 index , not 4 no index

print(a[:2]) # acess 2 index and print 0 to 1 index; here x:y ; x = starting index , y = access limit

print(a[2:]) # no limit start with 2 ; limit will be arrary size

print(a[-1]) #means start from last value

print('my favorite language is ',a)

print('%s is my favorite language'%a) 

ex = 2.846
print('desimal  : %.1f'%ex)

print('this is add %s and %.2f' %(a,ex)) #add just
h= 'health'
print(a + ' is string ' + h +' is not decsiaml number')

# print('is string '.join(a,h))

print('%s'.capitalize()%a) 
print('health'.upper()) #upper case
print('HEALTH'.casefold()) #small letter trans **
print('BANGLA'.lower())

print('BanGla'.swapcase()) #small convert into capital , capital conver into small letter

print(len(a)) #string length

# print(h.count('a')) #problem***

print(h.find('l')) #word index finder


k = "Bangladesh is my motherland , i love her very much."  
print(k.find('m')) 

print(k.find('a',2)) # find second letter

print(k.replace('a','A')) # word replace

print(k.replace(',', '')) #vanish

# print(k.strip('a')) #problem ***

print(k.split(' ')) 

