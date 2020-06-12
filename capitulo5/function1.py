# define our own functions
# def functionName(list of paremeters):
#	code detailing what the function should do
# return [expression]

def checkIfPrime (numberToCheck):
	for x in range(2, numberToCheck):
		if (numberToCheck%x == 0):
			return False
	return True

numberToCheck = int(input("check if number is prime, enter number: "))
answer = checkIfPrime(numberToCheck)
print(answer)

