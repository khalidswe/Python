myset = {'orange','mango','banana','jackfruit','cherry','orange',5,10.2} #type 1 

print(myset)   #double item will not print 
print(type(myset))
print(len(myset))

'''
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

myset.clear() #can clear this set

del myset #can delete this set


#loop set
for i in myset:
    print(i,end=' ')
'''
#join set

set1 = {"khalid","sifullah"}
set2 = {"shakib",5}
#print(set1.union(set2)) #by union
set1.update(set2)
print(set1) #by update

'''
add()	             Adds an element to the set
clear()	             Removes all the elements from the set
copy()  	         Returns a copy of the set
difference()         Returns a set containing the difference between two or more sets
difference_update()	 Removes the items in this set that are also included in another, specified set
discard()	         Remove the specified item
intersection()	     Returns a set, that is the intersection of two other sets
intersection_update()Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	     Returns whether two sets have a intersection or not
issubset()	         Returns whether another set contains this set or not
issuperset()	     Returns whether this set contains another set or not
pop()	             Removes an element from the set
remove()           	Removes the specified element
symmetric_difference()Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()               Return a set containing the union of sets
update()	          Update the set with the union of this set and others
'''