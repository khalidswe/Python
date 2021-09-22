mydictionary = {'name':'khalid sifullah','email':'khalidswe@outlook.com','contact no':['+8801521425853','+8801794922805']}

print(mydictionary)
print(type(mydictionary))
print(mydictionary["name"])
print(len(mydictionary))
'''
print(mydictionary.get('email')) 

print(mydictionary.keys()) #can print only keys
print(mydictionary.values()) #can print only values

mydictionary['email'] = 'khalid95-2520@diu.edu.bd' #can change item
print(mydictionary['email'])

mydictionary.update({'email':'khalid@gmail.com'}) #can update
print(mydictionary['email'])

mydictionary['age'] = 24 #add item
print(mydictionary)


del mydictionary['age'] #can remove with pop
print(mydictionary)

mydictionary.pop('email') #can remove with delete
print(mydictionary)

del mydictionary #can delete dict
print(mydictionary) #will not show anythong ,error


b = mydictionary.copy() #can copy dict
print(b)

if 'age' in mydictionary:
    print(mydictionary['age'])

#loop dict
for x in mydictionary:
    print(x, end=' ')

for x in mydictionary.values(): #same 
    print(x)

for x in mydictionary.keys(): #same
    print(x)
'''
#nested dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
'''
clear()	    Removes all the elements from the dictionary
copy()	    Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''