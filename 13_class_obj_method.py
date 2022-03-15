'''
class Calculator:

    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def division(self,a,b):
        if a == 0 or b == 0:
            print('its imposible to divide zero')   
        elif b > a:
           return b/a
        else:
            return a/b

calc1 = Calculator()

temp = calc1.addition(10,12)
print(temp)
temp = calc1.division(int(input('enter a: ')),int (input('enter b: ')))
print(temp)

calc2 = Calculator()
temp = calc1.multiply(10, 5)
print(temp)
temp = calc2.multiply(3, 10)
print(temp)

class Calculator2:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b

calc3 = Calculator2(20,12)
print(calc3.addition())
print(calc3.subtraction())
'''

class person:

    def __init__(self,name,age,blood_group,gender,mobile_no):
        self.name = name
        self.age = age
        self.blood_group = blood_group
        self.gender = gender
        self.mobile_no = mobile_no

    def printfucntion(self):
        print("\nName : "+self.name)
        print("Age : ",self.age)
        print("Blood Group : "+self.blood_group)
        print("Gender : "+self.gender)
        print("Mobile No : "+self.mobile_no)


khalid = person("khalid",24,"A+","Male","0152425853")
shakib = person("shakib",10,"B+","Male","0170466496")

shakib.printfucntion()
shakib.age = 24
khalid.printfucntion()
shakib.printfucntion()


