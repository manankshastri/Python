def is_prime(n):
    if (n>1):
        for i in range(2,n):
            if(n%i ==0):
                print(n,"is not Prime\n")
                break
        else:
            print(n,"is Prime\n")
    else:
        print(n,"is not Prime\n")


is_prime(31)

