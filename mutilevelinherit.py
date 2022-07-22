class shape:
    def show(self):
        print('function show')
class rect(shape):
    def display(self):
        print('function display')
class cube(rect):
    def dis(self):
        print('function dis')
obj=cube()
obj.show()
obj.display()
obj.dis()
