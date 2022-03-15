#match function:
'''
import re


pattern = r"^La"   # ^ sign for begging
mystring = "Lakhalid"

x = re.match(pattern,mystring)
print(x)

#search function:

import re

txt  = "we are learning python "

k = re.search("\s",txt) #would print the blackspace
print(k)
print(k.start()) #where blankspace started

l = re.search("Python",txt)
print(l) #will show none for Capital "P"

#re.IGNORECASE

s = re.search(r"Python",txt,re.IGNORECASE)
print(s.group()) #group will show the word


#replace function:
import re
text = "hey betty cooper, i am khalid"
print("before replaced: ",text)
result = re.sub(r"khalid","Jughead",text)

print("after replaced:",result)

result2 = re.sub(r"[A-Z]","B",result) #replaced in 1 position
print("again: ",result2)
'''

#assignment:

import re
mystring = "this is the string"

pattern = r"^thIS"
result = re.match(pattern,mystring,re.IGNORECASE)
print(result)

