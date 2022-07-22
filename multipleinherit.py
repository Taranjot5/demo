class shape:
    def show(self):
        print('function show')
class rect():
    def display(self):
        print('function display')
class cube(rect,shape):
    def dis(self):
        print('function dis')
obj=cube()
obj.show()
obj.display()
obj.dis()
