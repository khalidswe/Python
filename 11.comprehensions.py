'''
#list com
mylist = [x for x in range(20) if x % 2 == 0] # x = output , for x in range(20) = input ,if x % 2 == 0 = condition
print(mylist)

#set comp
myset = ['khalid','sifullah',20,2523]
printset = [x for x in myset ]
print(printset)

#dict comp
myitems = ['firstname','lastname','id']
myvalue = ['khalid','sifullah','2520']

prints = zip(myitems,myvalue)
print(list(prints)) 

'''
mydict = {'name' : 'khalid','age' : 20,'study' : 'diu' }

new_dict = {key : value for value , key in mydict.items()} #swaped 
print(new_dict)