# single inheritance
'''
class A :
    def func1(self): #parent class
        print("class A is called")

class B(A):
    def func2(self): #child class
        print("Class B is called")

obj = B() #always object will be in child class
obj.func1()
obj.func2()
'''
# multilevel inheritance
'''
class A :
    def func1(self): #parent class
        print("class A is called")

class B(A):
    def func2(self): #sub parent class
        print("Class B is called")
class C(B):
    def func3(self): #childc class
        print("Class C is here sir")

obj = C() #always object will be in child class
obj.func1()
obj.func2()
obj.func3()

'''
# multiple inheritance
'''
class A :
    def func1(self): #parent class
        print("class A is called")

class B:
    def func2(self): #another parent class
        print("Class B is called")
class C(A,B):
    def func3(self): #child class
        print("Class C is here sir")

obj = C() #always object will be in child class
obj.func1()
obj.func2()
obj.func3()
'''
# Hierarchical inheritance
'''
class A :
    def func1(self): #parent class
        print("class A is called")

class B(A):
    def func2(self): #child class
        print("Class B is called")
class C(A):
    def func3(self): #child class
        print("Class C is here sir")

#always object will be in child class
obj_B = B()
obj_B.func1()
obj_B.func2()

obj_C = C()
obj_C.func1()
obj_C.func3()

'''
# Hybrid Inheritance
class A :
    def func1(self): #parent class
        print("class A is called")

class B(A):
    def func2(self): #child class
        print("Class B is called")
class C(A):
    def func3(self): #child class
        print("Class C is here sir")
class D(B,C):
    def func4(self): #hybrid child class
        print("Class D is here sir!")

obj_D = D() #always object will be in child class

obj_D.func1()
obj_D.func2()
obj_D.func3()
obj_D.func4()

