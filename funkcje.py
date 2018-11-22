def f(x):
    return 2 * x ** 2 + 4 * x - 4

import math

def g(x):
    return math.sin(x) + math.cos(x)

def display(s):
    print(s)
    return

y = f(2)
print(y)
y = g(math.pi)
print("%.1f" % y)  # z dokładnością do 1 miejsca po przecinku
display(y)
