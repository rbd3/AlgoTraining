def fibonnacci(number):
    if number == 0:
        return 0
    elif number == 1:
     return 1
    else:
     return fibonnacci(number - 1) + fibonnacci(number - 2)
    
print(fibonnacci(24))

def fiboOptimize(number):
   a = 0
   b = 1
   fibo = 0
   
   if number == 0:
      return 0
   elif number == 1:
      return 1
   
   for _ in range(2, number + 1):
      fibo = a + b
      a = b
      b = fibo
   return fibo
   
   
   
print(fiboOptimize(24))