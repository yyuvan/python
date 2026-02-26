from abc import ABC, abstractclassmethod
class Animal(object):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can talk")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Snake(Animal):
    def move(self):
        print("I can slither")
class Lion(Animal):
    def move(self):
        print("I can roar")
R=Human()
R.move()

K=Snake()
K.move()

R=Dog()
R.move()

K=Lion()
K.move()