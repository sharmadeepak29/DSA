class BaseClass(object):
    def printHam(self):
        print("Ham")

class ChildClass(BaseClass):
    pass

x =ChildClass()
x.printHam()
