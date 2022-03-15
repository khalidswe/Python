# file creating

myfile = open('test.txt','w')
myfile.write("i'm new in file handling")
print('file added')
myfile.close()


#file openning

myfile= open('test.txt','r')
content = myfile.read()
print(content)
myfile.close()

myfile = open('test.txt','r')
value = myfile.read(5) #will show till index 5
print(value)
print(myfile.tell()) #confused
myfile.close()

list1 = ["python","c#","php","angular"]
file = open("test2 .txt","w")
file.writelines(list1)
print("file created")
file.close()
file= open("test2 .txt","r")
print(file.readlines())
file.close()


#append value in file

s = "sakib bhai bhalo lok , joy er mala tar ee hok"
file = open("test2 .txt","a")
file.write(s)
print("text addded")
file.close()

file = open("test2 .txt","r")
print(file.readlines())
file.close()


#assignment from learvern

#qs:1/2/3
print("\n\n")
new_file = open("assignment.txt","w")
temp = new_file.write("hello ")
print("text added sir")
new_file.close()

new_file = open("assignment.txt","r")
print(new_file.read())
new_file.close()

newtext = " shakib sir, good morning!"
new_file = open("assignment.txt","a")
new_file.write(newtext)
print("text added sir")
new_file.close()

new_file = open("assignment.txt","r")
print(new_file.readlines())

#qs 4/5
ass_list = ["apple","mango","orange"]
new_file2 = open("assignment2.txt","w")
new_file2.writelines(ass_list)
print("text added")
new_file2.close()

new_file2 = open("assignment2.txt","r")
print(new_file2.readlines())

newfile3= open("assignment2.txt","r")
newfile3.close()

#calender print
import calendar
year = int(input("\nenter year : "))
month = int(input("enter month : "))
print(calendar.month(year,month))