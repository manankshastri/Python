#function using iteration
def pd(n):                      
    prod =1
    for i in n:
        prod = prod *i
    return prod

#function using recursion
def pd1(n):                     
    if not n:
        return 1
    return n[0] * pd1(n[1:])

l = [1,2,3,4,5,6]
print("Using Iteration : ",pd(l))
print("Using Recursion : ",pd1(l))
