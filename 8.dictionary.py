mydictionary = {'name':'khalid sifullah','email':'khalidswe@outlook.com','contact no':['+8801521425853','+8801794922805']}

print(mydictionary)
print(type(mydictionary))
print(mydictionary["name"])
print(len(mydictionary))

print(mydictionary.get('email')) 

print(mydictionary.keys()) #can print only keys
print(mydictionary.values()) #can print only values

mydictionary['email'] = 'khalid95-2520@diu.edu.bd' #can change item
print(mydictionary['email'])

mydictionary.update({'email':'khalid@gmail.com'}) #can update
print(mydictionary['email'])

mydictionary['age'] = 24 #add item
print(mydictionary)

'''
del mydictionary['age'] #can remove with pop
print(mydictionary)

mydictionary.pop('email') #can remove with delete
print(mydictionary)

del mydictionary #can delete dict
print(mydictionary) #will not show anythong ,error
'''

b = mydictionary.copy() #can copy dict
print(b)

if 'age' in mydictionary:
    print(mydictionary['age'])


