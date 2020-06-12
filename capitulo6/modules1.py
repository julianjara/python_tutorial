#Consider a module to be the same as a code library.
#A file containing a set of functions you want to 
#include in your application.
import random
print("Printing random number using random.random()")
print(random.random())

# the following prints a random within a range
import random
print("Random integer is", random.randint(0, 9))

# the following is within a range and a step
import random
print("Random integer, range 2-20, step 2, is", random.randrange(2, 20, 2))