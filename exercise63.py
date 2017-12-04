def is_prime(n):
  for k in range(2,n):
      prime = True
      for i in range(2,k):
              if(k%i ==0):
                  prime = False
      if prime:
          print(k , end = " ")

is_prime(100)