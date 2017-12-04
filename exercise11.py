def pd(n):                      #function using iteration
    prod =1
    for i in n:
        prod = prod *i
    return prod

def pd1(n):                     #function using recursion
    if not n:
        return 1
    return n[0] * pd1(n[1:])

l = [1,2,3,4,5,6]
print("Using Iteration : ",pd(l))
print("Using Recursion : ",pd1(l))