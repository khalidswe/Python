#list create
list = [] #blank list
mylist = ["apple","orange","banana","mango",50]

print(mylist)
print(type(list))
print(len(mylist)) 

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
del mylist #delete the list
print(mylist) 

mylist.clear() #clear all data
print(mylist)
'''

for x in mylist: # loop all data
    print(x)


for i in range(len(mylist)):
    print(mylist[i])

mylist.reverse() #reverse list
print(mylist)

mylist.sort() #sorting
print(mylist)

