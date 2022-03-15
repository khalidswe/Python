#list create
list = [] #blank list
mylist = ["apple","orange","banana","mango",50]

print(mylist)
print(type(list))
print(len(mylist)) 
'''
print(mylist[3])
print(mylist[-1])
print(mylist[:3])
print(type(mylist[1]))

if "apple" in mylist:
    print("yes, it is")

mylist[1] = "malta" #change value
print(mylist)

mylist[1:3]="orange", "grape" #change nultiple
print(mylist)

mylist.insert(1, "jackfruit") #insert value in index
print(mylist)

mylist.append(100.014)
print(mylist) #insert in last

sublist = ["taka","car"]  
mylist.extend(sublist) #twi list add/extend
print(mylist)

tupleadd = ("kiwi","money") 
mylist.extend(tupleadd) #tuple add/extend
print(mylist)

mylist.remove("kiwi") #remove value
print(mylist)

mylist.pop(6) #pop by index
print(mylist)

mylist.pop() #pop automatic remove last index
print(mylist)

del mylist[5] #delete 
print(mylist)
'''

''' 
del mylist #delete the list
print(mylist) 

mylist.clear() #clear all data
print(mylist)


for x in mylist: # loop all data
    print(x)


for i in range(len(mylist)):
    print(mylist[i])

mylist.reverse() #reverse list
print(mylist)

mylist.sort() #sorting
print(mylist)

newlist = []
 
for x in mylist:
    if "ap" in x:
        newlist.append(x)

newlist = [x for x in mylist if "ap" in x] #same in line code
print(newlist) 

newlist = [x for x in mylist if x != "apple"]
print(newlist) 
'''
#list sorting
newlist = ["apple","orange","banana","mango"]
newlist.sort() #sorting list
print(newlist)

newlist2 = [10,2,5,100,50,30,400,20,12]
newlist2.sort(reverse=True) #decending
print(newlist2)

#copy list
copy_list = newlist.copy() #copied from newlist to copy_list
print(copy_list)

#join list
print('new list = ',newlist+newlist2)

for x in newlist2: #same thing by append
    newlist.append(x)
print(newlist)

newlist.extend(newlist2)#same thing by extend
print(newlist)

'''
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()     	Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

'''
