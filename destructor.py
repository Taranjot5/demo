class A:
    def __init__(self):
        print('constructor')
    def display(self):
        print('method display')
    def __del__(self):
        print('destructor')
obj=A()
obj.display()
del obj
obj.display()
