a=int(input("Number: "))
b=int(input("Number: "))
func=input("What function? (+,-,*,/) ")
def add(a,b): 
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divid(a,b):
     return a/b
if func=="+":
    print(add(a,b))
elif func=="-":
    print(sub(a,b))
elif func=="*":
    print(multi(a,b))
elif func=="/":
    print(divid(a,b))

