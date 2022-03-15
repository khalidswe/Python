from tkinter import *

r = Tk()
r.geometry("500x300")
r.title("3idiots")
r.configure(bg="#2E8B57")

#widgets:
student_id = Label(r,text="Student ID: ")
student_id.place(x=150,y=20)

name =Label(r,text="Student Name: ")
name.place(x=150,y=60)

email =Label(r,text="Email: ")
email.place(x=150,y=100)

dept =Label(r,text="Department: ")
dept.place(x=150,y=140)

#entry :

student_id_entry =Entry()
student_id_entry.place(x=250,y=20)

name_entry =Entry()
name_entry.place(x=250,y=60)

email_entry =Entry()
email_entry.place(x=250,y=100)

dept_entry =Entry()
dept_entry.place(x=250,y=140)

#button:

insertbutton = Button(r,text = " Insert ",bg = "white")
insertbutton.place(x = 250,y=200)




mainloop()