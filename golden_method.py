from math import sqrt

golden_ratio = (sqrt(5) + 1) / 2

def golden_method(f, a, b, n):
  if n == 0:
    return f((a + b) / 2.0)

  l = b - a
  left = b - l / golden_ratio
  right = a + l / golden_ratio

  new_a = a
  new_b = b

  if f(left) > f(right):
    new_a = left
  else:
    new_b = right
  
  return golden_search(f, new_a, new_b, n-1)
