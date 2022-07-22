class animal():
    def sleep(self):
        print('animal is sleeping')
class dog(animal):
    def loyal(self):
        print('dog is loyal animal')
class cat(animal):
    def cute(self):
        print('cat are so cute')
obj=dog()
obj.sleep()
obj.loyal()
obj1=cat()
obj1.sleep()
obj1.cute()
