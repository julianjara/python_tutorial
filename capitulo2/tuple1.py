# Tuple is a like a list but you cannot modify their values.
# the initial values are the values that will stay for the rest of the program
# example the name of the months of the year
# tuple = (initial values)  notice the parenthesis
tuple = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print(tuple)

print("My birthday is on ")
print(tuple[8])

# print a subset of the tuple
print(tuple[2:5])

# print with a stepper
print(tuple[0:10:3])