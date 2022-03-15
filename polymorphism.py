# method overloading / compile time polymorphism
'''
class MO:
    def myFunction(self):
        print("this is number 1")

    def myFunction(self,a):
        print("this is number 2")

    def myFunction(self,a,b):
        print("this is number 3")

obj = MO()
obj.myFunction(10)
'''
#this code won't run cause this method is overloading polymorphism



# method overriding / runtime polymorphism
'''
class a:
    def a1(self,k):
        print("this is number 1")
class b(a):
    def a1(self,k):
        print("this is number 2")
        super().a1(10)

class c(b):
    def a1(self,k):
        print("this is number 3")
        super().a1(10)


obj1 = c()
obj1.a1(10) # we have create super for other method

'''