#Consider a module to be the same as a code library.
#A file containing a set of functions you want to 
#include in your application.

#for some functions you don't need to import
newString = "Hello World".replace("World", "Universe")
print(newString)

#other functions need to be imported
import random
print("Printing random number using random.random()")
print(random.random())

# the following prints a random within a range
import random
print("Random integer between 0-9 =", random.randint(0, 9))

# the following is within a range and a step
import random
print("Random integer, range 2-20, step 2, is =", random.randrange(2, 20, 2))