# the following function prints nombre y apellido
def myfunction(nombre, apellido):
	print(nombre + " " + apellido)

myfunction("Julian", "Jaramillo")

# the following function receives a random number of parameters
print("the following function receives a random number of parameters")
def myfunction2(*kids):
	print("the youngest child is:" + kids[2])

myfunction2("Felipe", "Julian", "Veronica")

# the following example returns a value
print("The following example returns a value")
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
