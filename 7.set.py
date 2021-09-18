myset = {'orange','mango','banana','jackfruit','cherry','orange',5,10.2} #type 1 

print(myset)   #double item will not print 
print(type(myset))
print(len(myset))

a = set('abracadabra') #type 2
print(a)
print(type(a))

b = {} #new set
c = set() #new set
print(type(b)) #this is not set , it will show  <class "dict"> (dictionary)
print(type(c))

print("mango" in myset) 

myset.add(100.20) #we can add item
print(myset)

add_set = {"dove","band"} #new set
myset.update(add_set) #we can add 2 set into 1
print(myset)

mylist = ["kiwi"] #new list
myset.update(mylist) #we can add item from list also
print(myset)

myset.remove("kiwi") #can remove item type 1 , if not in set, will show error 
myset.discard(100.20)  #type 2 , if not in set, will not show error
x = myset.pop() #can pop 1st item
print(x) #poped item
print(myset)

'''
myset.clear() #can clear this set

del myset #can delete this set
'''


