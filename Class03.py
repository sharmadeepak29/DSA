class BaseClass:
    def test(self):
        print("ham")

class Derived(BaseClass):
    def test(self):
        print("hammer")

i = Derived()
i.test()
""" x = BaseClass()
print(i.x)
print(x.x) """