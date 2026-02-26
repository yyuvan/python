class Person(object):
    def __init__(self, fname, lname, age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def display(self):
        print(self.fname)
        print(self.lname)
        print(self.age)
class student(Person):
    def __init__(self, fname, lname, age, gradyear):
        self.gradyear=gradyear
        Person.__init__(self,fname,lname,age)
a=student("Chris","Tyson",2009,2027)
a.display()

        