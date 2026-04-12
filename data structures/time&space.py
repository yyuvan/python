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


