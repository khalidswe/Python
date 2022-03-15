
import pymysql

def createConection(): #creating connection to database
    return pymysql.connect(host="localhost", database="pythonlearnvern",user="root",password="",port=3306)

def createTable(): #creating table
    conn = createConection()
    cursor = conn.cursor() #helping to execute query
    query = "create table student(s_id VARCHAR(20) primary key,name VARCHAR(50),email VARCHAR(30),department VARCHAR(30))"
    cursor.execute(query)
    conn.commit()
    print("table created!")
    conn.close()

#createTable()

#data insertion in database:

def InsertionData(s_id,name,email,department):
    conn = createConection()
    cursor = conn.cursor()
    args = (s_id,name,email,department)
    query = "insert into student(s_id,name,email,department) values(%s,%s,%s,%s)"
    cursor.execute(query,args)
    conn.commit()
    print("data inserted!")
    conn.close()

n = int(input("how many students data want to add: "))
for i in range(0,n):
    student_id = input("id : ")
    name = input("name : ")
    email = input("email : ")
    department = input("department : ")
    InsertionData(student_id,name,email,department)
    n = n + 1

#fetch all data :
def fetchalldata():
    conn = createConection()
    cursor = conn.cursor()
    query = "select * from student"
    cursor.execute(query)
    result = cursor.fetchall()

    for i in result:
        print(i)
fetchalldata()

#fetch only 1 data by id:

def fetchOneData(student_id):
    conn = createConection()
    cursor = conn.cursor()
    args =(student_id)
    query = "select * from student where s_id=%s"
    cursor.execute(query,args)
    res = cursor.fetchall()

    for i in res:
        print(i)

student_id = input("enter id : ")
fetchOneData(student_id)