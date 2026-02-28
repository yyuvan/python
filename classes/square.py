class computer:
    def __init__(self):
        self.mp=0
    def sell(self):
        print("Selling Price: ", self.mp-(self.mp*0.2))
        print("Max price: ", self.mp)
    def smp(self, price):
        self.mp=price
ob=computer()
# ob.mp=int(input("What is your max-price? "))
ob.smp(1000)
ob.sell()