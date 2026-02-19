class Parrot:
    def __init__(self, age, name, colour):
        self.age=age
        self.name=name
        self.colour=colour
    def intro(self):
        print("Hi my name is", self.name)
ob=Parrot(15,"Hosea", "blue")
ob.intro()
print("My age is ", ob.age)
print("I am ", ob.colour)