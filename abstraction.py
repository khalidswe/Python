class absClass:
    def absMethod(self):
        pass

class khalid(absClass):
    def absMethod(self):
        print("this is khalid class")

class shakib(absClass):
    def absMethod(self):
        print("this is shakib class")

obj_khalid = khalid()
obj_shakib = shakib()

obj_khalid.absMethod()
obj_shakib.absMethod()


class animal:
    def nature(self):
        pass

class dog(animal):
    def nature(self):
        print("its dog class")

class cow(animal):
    def nature(self):
        print("its cow class")

obj_dog = dog()
obj_dog.nature()

obj_cow = cow()
obj_cow.nature()
