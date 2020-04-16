class A():
    def __init__(self):
        self.name=1

    def get_name(self):
        name=self.name+1

a=A()
print(a.get_name())