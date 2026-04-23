
#Target Question:
import time
def targetarr(arr, target):
    if target not in arr:
        print("-1")
    else:
        for i in range(len(arr)):
            if arr[i]==target:
                print(i)
                break
start=time.time()
targetarr([1, 2, 2, 2, 3, 4, 5],2)
end=time.time()
print(end-start)


#Binary Method:
def binary(arr,target):
    arr_lenght=len(arr)
    left, right=0,arr_lenght-1
    while left <=right:
        middle = (left + right) // 2
        if target==arr[middle]:
            return middle
            break
        elif target>arr[middle]:
            left=middle+1
        elif target<arr[middle]:
            right=middle-1
    return -1
start=time.time()
print(binary([1, 2, 2, 2, 3, 4, 5],2))
end=time.time()
print(end-start)
   

# def printnumber(n):
#     iteration=0
#     print("NUmber: " ,n)
#     iteration+=1
#     print('Total is', iteration,'\n')
# printnumber(10)
# printnumber(20)

import time
def it(n):
    start=time.time()
    for i in range(n):
        print(i, end=" ")
    end=time.time()
    print(f"time: {end-start}")
it(10000000)