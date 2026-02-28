class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"My name is {self.name} the cat and I am {self.age} years old.")
    def make_sound(self):
        print("Purrrrrrrrrrr")
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"My name is {self.name} the dog and I am {self.age} years old.")
    def make_sound(self):
        print("Wooofffffffff!")
cat1=Cat("Dodo", 2.5)
dog1=Dog("Tyson", 8)

for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()