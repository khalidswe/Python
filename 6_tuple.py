mytuple = ("cod","gta5","csgo","valorant","pubg",5,10.20)

print(mytuple)
'''
print(type(mytuple))
print(mytuple[2])
print(mytuple[1:4])
print(mytuple[:3])
print(type(mytuple[5]))

mytuple = mytuple + (50,"apex legend","valorant",) #added in last just
print(mytuple)

print(len(mytuple))
print(mytuple.count("valorant"))

if "valorant" in mytuple:
    print("yes , valorant there bro\n")

# we can add item , first we have to convert tuple to list then add and back to tuple
newtuple  = list(mytuple)

print(type(newtuple)) #see change

newtuple.append("far cry")
mytuple = tuple(newtuple)

print(mytuple)

# tuple to tuple add
addtuple = ("visual studio code",500,)

mytuple += addtuple
print(mytuple) #added all item

#remove same process tuple to list
rev_tuple = list(mytuple)

rev_tuple.remove("visual studio code")
print(rev_tuple)

mytuple = tuple(rev_tuple)
print(type(mytuple))

# we can delete but it will delete full tuple

del mytuple
print(mytuple) #will not show any tuple

game = mytuple  #unpack
 
(cd,vl,*pbg) = game #asterisk

print(cd)
print(vl)
print(pbg)

(cd,*vl,pbg) = game #asterisk

print(cd)
print(vl)
print(pbg)
'''
#loop tuple
'''
for x in mytuple:
   print(x,end=' ')

for i in range(len(mytuple)): #same 
    print(mytuple[i],end=' ')

x=0
while x < len(mytuple):
    print(mytuple[x],end=' ')
    x+=1
'''
#join tuple

newtuple = ("khalid","sifullah")
newtuple2 = ("shakib","mahmud")
print(newtuple+newtuple2)

#multiply join 
print(newtuple*2) 

'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''