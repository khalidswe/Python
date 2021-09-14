mytuple = ("cod","gta5","csgo","valorant","pubg",5,10.20)

print(mytuple)

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

##del mytuple
##print(mytuple) #will not show any tuple

