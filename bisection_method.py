def bisection_method(f, f_prime, a, b, n):
  if n == 0:
    return f((a + b) / 2)

  m = (a + b) / 2.0
  m_value = f_prime(m)

  new_a = a
  new_b = b

  if m_value < 0:
    new_a = m
  else:
    new_b = m
  
  return bisection_method(f, f_prime, new_a, new_b, n-1)

