from math import sqrt

def fibonacci_method(f, a, b, n):
  if n == 0:
    return f((a + b) / 2.0)

  r = 1 - float(fibonacci(n+1)) / fibonacci(n+2)
  l = b - a
  left = a + r * l
  right = b - r * l

  new_a = a
  new_b = b

  if f(left) > f(right):
    new_a = left
  else:
    new_b = right
  
  return fibonacci_search(f, new_a, new_b, n-1)

def fibonacci(n):
  if n <= 2:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

