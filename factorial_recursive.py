def factorial(n):
  if n == 1:
    return n
  else:
    return n * factorial(n - 1)

n = 23
fact = factorial(n)
      
print ('The factorial of', n, 'is:', fact)
