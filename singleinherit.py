class A:
    def fa(self):
        print('parent class')
class B(A):
    def fb(self):
        print('base class')
obj=B()
obj.fa()
obj.fb()
