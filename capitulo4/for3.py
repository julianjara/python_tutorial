# loop through a dictionary
age = {'Peter': 29, 'John': 22, 'Ramon': 32, 'Juan': 15, 'Mary': 4}
for i in age:
	print(i)

print("Now lets print along with the age")
for i in age:
	print("Name = %s, Age = %d" % (i, age[i]))

print("Alternatively we can use the items() method which is a built-in method that returns each of the dictionary kay pairs")
for i, j in age.items():
	print("Name = %s, Age = %d" % (i, j))