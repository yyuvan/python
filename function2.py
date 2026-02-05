# Factorial of 1 is 1
# Factorial of 2 is 2
# Factorial 3 is 6
# Factorial of 4 is 24

num=int(input("Number: "))

# def fact():
#     i=num
#     f=1
#     while i>0:
#         f=f*i
#         i=i-1
#     print(f"The factorial is {f}")
# fact()

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(num))
    
        

