# modules help because they contain a lot of code that already do a lot of things
# for example the math module, instead of writting code to calculate factorial we use the math module

import math

num = int(input("factorial de = "))
print(math.factorial(num))

print("El valor de pi es =",math.pi)

print(dir(math))