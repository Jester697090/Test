print("Any text")

n = 5

if n > 7:
    print("True")
else:
    print("False")

# To comment single line

""" To comment
multiple lines - 
so called - docstrings"""

s = "Some string"

print(s)

s = 10  # Can be as well int or str

print(s)

age = 22
Age = 23
AGE = 24

print(age, Age, AGE)  # Three different variables; print(s, t) - separated with space " "

print("My age is " + str(age) + ".")  # String concat

a = 12
b = 1.2
c = 12j

print(type(a), type(b), type(c))  # Types (classes) of numeric variables

d = 12e5
e = 1.2e-3

print(type(d), type(e))  # Scientific numbers are float class

f = 3 + 5j

print(type(f))  # Every number of a + bj is complex

g = int(b)  # Is 1
h = float(a)  # Is still 12 but float class (12.0)

s = str(b)  # String
k = float(s)  # Parsed to float

print(g, h, s, k)

# Formatowanie
# %s - string, %d - całkowita, %f - zmiennoprzecinkowa, %x - heksadecymalna

print("Trzy miejsca po przecinku liczby k: %.3f" % k)
