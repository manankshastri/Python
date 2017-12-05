#function prints the fibonacci series
def fib(n):
    f0 = 0
    f1 = 1
    print("Fibonacci Series: ")
    for i in range(n):
        print(f0, end = " ")            #end = " " - to print all the elements in a single line
        fn = f0 +f1
        f0 = f1
        f1 = fn

fib(6)                  #prints first six numbers 
