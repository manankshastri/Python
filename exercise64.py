def is_prime(n, l):
    count = 0
    for k in range(2, n):
        prime = True
        for i in range(2, k):
            if (k % i == 0):
                prime = False

        if prime:
            if (count < l):
                print("Prime ({}) : {} ".format(count + 1, k))
                count += 1


is_prime(100, 10)