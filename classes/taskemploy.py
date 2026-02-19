#Every emplyee has a unique ID and grade. Based on their grade. I want to create a class covering the employees inside salary, grade, ID 
class employees:
    def __init__(self, employee, grade, ID):
        self.employee=employee
        self.grade=grade
        self.ID=ID
    def sal(self):
        if self.grade=="A":
            return "165,000"
        elif self.grade=="B":
            return "125,000"
        elif self.grade=="C":
            return "85,000"
        else:
            return "65,000"
ob=employees("Suresh","A","018292")
ob1=employees("Arthur","C","092092")
ob2=employees("Brian","D","0283202")
print(ob.employee,ob.grade,ob.ID,ob.sal())
print(ob1.employee,ob1.grade,ob1.ID,ob1.sal())
print(ob2.employee,ob2.grade,ob2.ID,ob2.sal())
            

