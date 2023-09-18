import time

startTime = time.time()

# code
for n in range(2, 100000):
    for i in range(2, n):
        if n % i == 0:
            print(n, '=', i, '*', n//i)
            break
    else:
        print(n, 'is prime number !')

endTime = time.time()
totalTime = endTime - startTime
print("Total time to excute the code is - ", totalTime)
