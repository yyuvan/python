# x=10
# y=4
# print("num1 and & AND num2=", x & y)
# print("\n num1 | or num2=", x|y)
# print(" num1 ~ NOT", ~x)
# print("\n num1 ^ XOR num2=", x^y)

# print("\n x right =", x>>1)
# print("\n y right =", y>>1)

# print("\n x left =", x<<1)
# print("\n y left =", y<<1)

# def isEvenOdd(n):
#     if (n^1==n+1):
#         return True
#     else: 
#         return False
# number=int(input("Num: "))
# if isEvenOdd(number):
#     print(number, "is even")
# else:
#     print(number, "is odd3")
def numberOfBits(n):
    count=0
    while n:
        count+=1
        n>>=1
    return count
number=int(input("Num: "))
print("Total bits: ",numberOfBits(number))