# lambda functions can have many arguments but only one expression
# lambda arguments : expression

# in the following example argument is a
# then the expression does a + 10
x = lambda a : a + 10
print(x(5))

#another example of lambda where there are multiple arguments
x = lambda a, b : a * b
print(x(4, 5))