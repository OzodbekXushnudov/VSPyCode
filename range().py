for n in range(2, 100):
    for i in range(2, n):
        if n % i == 0:
            print(n, '=', i, '*', n//i)
            break
    else:
        print(n, 'is prime number !')
