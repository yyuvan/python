# #factor problem
'''
import time

x=int(input("Enter the number: "))
facts=[]

start=time.time()
count=0
for i in range(1,x+1):
    if x%i==0:
        # facts.append(i)
        count+=1
end=time.time()
print(facts)
print("Time taken:", end - start, "seconds")


count=0
start=time.time()
for i in range(1, int(x**(0.5))+1):
    if  i % i==0:
        if x%i !=i:
            count+=2
        else:
            count +=2
end =time.time()
print(count)
print(end-start)
'''
mytuple=(3,4,5,7,5,2,6,5,2,34,6,7,87)
# print(mytuple[0])
# mytuple[0]=4
# print(mytuple)
# print(mytuple.count(5))
# print(mytuple.index(5))


#PRACTICE QUESTION'

# USER INPUT LEFT TO RIGHT SAME MEANS PALINDROME
#WRITE PROGRAM TO RUN IF NUM IS PALINDROME

# x=int(input("Number: "))
# x=list(x)
# print(x)
# y=len(x)
# # print(y)
# if x==x[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")        

# ognum=x
# reversenum=0
# while x>0:
#     digit=x%10
#     reversenum=reversenum*10+digit
#     x//=10
# if ognum==reversenum:
#     print("Palindrome")
# else:
#     print("Not palindrome")        



#HCF:

# x=int(input("LOWER NUM: "))
# y=int(input("HIGHER NUM: "))
# xandyfactors=[]
    
# for i in range(1,x+1):
#     if x%i==0 and y%i==0:
#         factor=i
# print(i)

# ages=[18,29,39,29,292,191,1929,29,19,2,3,4,5,7,0]
# for i in range(len(ages)):
#     if ages[i] >=18:
#         print(ages[i])
        
'''
#PRIME NUMBER
x=int(input("Num: "))
primenum=[]

for i in range(1,x+1):
    factors=[]
    for j in range(2,i+1):
        if i%j==0:
            factors.append(j)
    if len(factors)<2:
        primenum.append(i)

    
print(primenum)
'''

# #SECOND CODE
# from math import sqrt 
# number=int(input("Num: "))
# if number>1:
#     for i in range(2, int(sqrt(number))+1):

#         if (number % i) == 0:
#             print(input, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")
# else:
#     print(number, "is a prime number")


def Sieve(num):
    prime=[ True for i in range(num+1)]
    p=2
    while (p*p<=num):
        if (prime[p]==True):
            for i in range(p*p, num+1,p):
                prime[i]=False
        p+=1
    
    for p in range(2, num+1):
        if prime[p]:
            print(p)
num=int(input("Num: "))
# print("Printing following prime numbers less than ", num)
# Sieve(num)
num = int(input("Enter number: "))

for i in range(1, num + 1):
    print("\nChecking number:", i)

    c = 0
    temp = i
    rev = 0

    # Check if prime
    for j in range(1, temp + 1):
        if temp % j == 0:
            c += 1

    print("Number of factors:", c)

    if c == 2:
        print(i, "is a prime number")

        # Reverse the number
        temp2 = i
        while temp2 > 0:
            digit = temp2 % 10
            rev = rev * 10 + digit
            temp2 //= 10

        print("Reversed number:", rev)

        if rev == i:
            print("👉", i, "is a PRIME PALINDROME")
        else:
            print(i, "is prime but not palindrome")

    else:
        print(i, "is not a prime number")