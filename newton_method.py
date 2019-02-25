def newton_method(f, f_prime, f_prime_prime, a, b, n):
  p = (a + b) / 2.0
  for i in range(0, n):
    p -= float(f_prime(p)) / f_prime_prime(p)
  return f(p)