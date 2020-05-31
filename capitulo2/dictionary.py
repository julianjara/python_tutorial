# Dictionary is a collection of related data PAIRS
# for example the username and age of 5 people
# dictionary = {dictionary key : data}
# with the requirement that dictionary keys must be unique (within one dictionary)
# for example this is an error:
# dictionary = {"Peter":38, "John":51, "Peter":13}
userNameAndAge = {"Peter":38, "John":51, "Alex":13, "Alvin":"Not Available"}

#you can also declare the same dictionary like this:
userNameAndAge2 = dict(Peter = 38, John = 51, Alex = 13, Alvin ="Not Available")
print(userNameAndAge)

print("checking Alex Age")
print(userNameAndAge["Alex"])

print("Modifying Alex' Age to 15")
userNameAndAge["Alex"] = 15
print(userNameAndAge["Alex"])

# to add to the dictionary
userNameAndAge["Joe"] = 40
print(userNameAndAge)

# to delete from a dictionary
del userNameAndAge["Joe"]
print(userNameAndAge)

# we can declare a dictionary with no values
userNameAndAge3 = {}