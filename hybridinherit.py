class animal():
    def types(self):
        print('animal is of two types domestic and wild')
class dog(animal):
    def loyal(self):
        print('dog are very loyal')
class cat(animal):
    def cute(self):
        print('cat are so cute')
class domestic(dog,cat):
    def animals(self):
        print('cat and dog are domestic animal')
obj=domestic()
obj.animals()
obj.loyal()
obj.cute()
obj.types()
