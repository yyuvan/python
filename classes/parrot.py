class Parrot:
    species="Bird"
    def __init__(self, name, age):
        self.name=name
        self.age= age

ob=Parrot("Jolly",8)
print("The parrot is",ob.age)
print("The parrots name is",ob.name)
print("The parrot is a", ob.species)
