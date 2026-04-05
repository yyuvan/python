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