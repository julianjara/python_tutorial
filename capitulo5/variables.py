# global variables are available globally
# local variables are available only within a function
message1 = "Global Message"
def myFunction():
	print("\nInside the function")
	print(message1)
	message2 = "Local variable"
	print(message2)

myFunction()

print("\nOutside the function")
print(message1)
print(message2)

# print(message2) should throw an error because is not accesible outside the function