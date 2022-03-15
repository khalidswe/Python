# Private encapsulation
'''
class A:
    def __init__(self,a):
        self.__a =a

    def printfuncA(self):
        print("here is a : ",self.__a)

class B(A):
    def __init__(self,b):
        super().__init__(b)

    def printfuncB(self):
        print("here is b : ",self.__a)

obj_B = B(20)
obj_B.printfuncB() #wont run for being private
'''
# Protected encapsulation
'''
class A:
    def __init__(self,a):
        self._a =a

    def printfuncA(self):
        print("here is a : ",self._a)

class B(A):
    def __init__(self,b):
        super().__init__(b)

    def printfuncB(self):
        print("here is b : ",self._a)

obj_B = B(20)
obj_B.printfuncB()
'''

#assignment of OOPS from learnvern

class Vehicle:
    def printfunc(self,a):
        print("hi this is vehicle class and a is :",a)

class bus(Vehicle):
    def printfunc(self,a):
        print("this is vehile class and a is : ",a)
        super().printfunc(10)
class truck(bus):
    def printfunc(self,a):
        print("this is bus class and a is : ",a)
        super().printfunc(10)

obj_truck = truck()
obj_truck.printfunc(10)
