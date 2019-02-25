from golden_method import golden_method
from fibonacci_method import fibonacci_method
from bisection_method import bisection_method
from newton_method import newton_method

from math import e, log, pow, exp

foo = lambda x: log(pow(x, 2) - 1.6*x + 3, e)
foo_prime = lambda x: (2*x - 1.6) / (pow(x, 2) - 1.6 * x + 3)
foo_prime_prime = lambda x: (-2*(pow(x, 2) - 1.6*x - 1.72)) / ((pow(x, 2) - 1.6 * x + 3) ** 2)

bar = lambda x: (x-1) * exp(-2*pow(x, 2) + 4*x)
bar_prime = lambda x: exp(-2 * x ** 2 + 4 * x) + (x - 1) * exp(-2 * x ** 2 + 4 * x) * (-4 * x + 4)
bar_prime_prime = lambda x: 4 * exp(-2 * (x - 2) * x) * (4 * x ** 3 - 12 * x ** 2 + 9 * x - 1)


# Golden Search
# print golden_method(foo, 0, 3, 2) #0.880270585397
# print golden_method(foo, 0, 3, 4) #0.865478143955
# print golden_method(foo, 0, 3, 8) #0.858668371569
# print golden_method(foo, 0, 3, 16) #0.858661631817

# Fibonacci Search
# print fibonacci_method(foo, 0, 3, 2) #0.896088024557
# print fibonacci_method(foo, 0, 3, 4) #0.882281415771
# print fibonacci_method(foo, 0, 3, 8) #0.858696637335
# print fibonacci_method(foo, 0, 3, 16) #0.858661802438

# Bisection Method
# print bisection_method(foo, foo_prime, 0, 3, 2) #0.902445325052
# print bisection_method(foo, foo_prime, 0, 3, 4) #0.859472333752
# print bisection_method(foo, foo_prime, 0, 3, 8) #0.858664787171
# print bisection_method(foo, foo_prime, 0, 3, 16) #0.858661619086

# Newton Method
# print newton_method(foo, foo_prime, foo_prime_prime, 0, 3, 2) #0.859495369591
# print newton_method(foo, foo_prime, foo_prime_prime, 0, 3, 4) #0.858661619038
# print newton_method(foo, foo_prime, foo_prime_prime, 0, 3, 8) #0.858661619038
# print newton_method(foo, foo_prime, foo_prime_prime, 0, 3, 16) #0.858661619038

# Golden Search
# print golden_method(bar, 0, 3, 2) #-2.1910985546
# print golden_method(bar, 0, 3, 4) #-2.2398365178
# print golden_method(bar, 0, 3, 8) #-2.24009943119
# print golden_method(bar, 0, 3, 16) #-2.24084452538

# Fibonacci Search
# print fibonacci_method(bar, 0, 3, 2) #-2.24084453517
# print fibonacci_method(bar, 0, 3, 4) #-1.60327455585
# print fibonacci_method(bar, 0, 3, 8) #-2.22929452136
# print fibonacci_method(bar, 0, 3, 16) #-2.24084419961

# Bisection Method
# print bisection_method(bar, bar_prime, 0, 3, 2) #-2.11434774631
# print bisection_method(bar, bar_prime, 0, 3, 4) #-2.23228185631
# print bisection_method(bar, bar_prime, 0, 3, 8) #-2.24081038725
# print bisection_method(bar, bar_prime, 0, 3, 16) #-2.24084453465

# Newton Method
# print newton_method(bar, bar_prime, bar_prime_prime, 0, 3, 2) #2.24084453517
# print newton_method(bar, bar_prime, bar_prime_prime, 0, 3, 4) #2.24084453517
# print newton_method(bar, bar_prime, bar_prime_prime, 0, 3, 8) #2.24084453517
# print newton_method(bar, bar_prime, bar_prime_prime, 0, 3, 16) #2.24084453517

# Golden Search
# print golden_method(bar, -1, 1, 2) #-2.10808569553
# print golden_method(bar, -1, 1, 4) #-2.20474694004
# print golden_method(bar, -1, 1, 8) #-2.24045502781
# print golden_method(bar, -1, 1, 16) #-2.24084419952

# Fibonacci Search
# print fibonacci_method(bar, -1, 1, 2) #-1.0
# print fibonacci_method(bar, -1, 1, 4) #-2.11434774631
# print fibonacci_method(bar, -1, 1, 8) #-2.23430359052
# print fibonacci_method(bar, -1, 1, 16) #-2.2408431931

# Bisection Method
# print bisection_method(bar, bar_prime, -1, 1, 2) #-1.79915647048
# print bisection_method(bar, bar_prime, -1, 1, 4) #-2.20741766532
# print bisection_method(bar, bar_prime, -1, 1, 8) #-2.24070812312
# print bisection_method(bar, bar_prime, -1, 1, 16) #-2.24084453308

# Newton Method
# print newton_method(bar, bar_prime, bar_prime_prime, -1, 1, 2) #-0.00867493809132
# print newton_method(bar, bar_prime, bar_prime_prime, -1, 1, 4) #-0.000910893802618
# print newton_method(bar, bar_prime, bar_prime_prime, -1, 1, 8) #-1.20670935307e-05
# print newton_method(bar, bar_prime, bar_prime_prime, -1, 1, 16) #-2.75639440602e-09