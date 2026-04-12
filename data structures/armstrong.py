# x=input("Number: ")
# z=len(x)
# t=0

# for d in x:
#     t+=int(d)**z
# if t == int(x):
#     print("True")
# else:
#     print("False")

#FACTORIAL:

def factorial(x):
    t=1
    for i in range(1,x+1):
        t=t*i
    print(t)
    
factorial(7)



