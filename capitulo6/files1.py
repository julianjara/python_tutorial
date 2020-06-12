# when you need to input a lot of data is best to have it on a separte file and use
# a module to read it

# we will create a file called text.txt and read it
# 'r' read only, other options are 
# 'w' write - if the file doesn't exist it will create it
# 'r+' for both reading an writting
# 'a' for appending - if the file doesn't exist it will create it

f = open('text.txt', 'r')

# each time you call readline it will read a new line from the file
firstline = f.readline()
secondline = f.readline()
print(firstline)
print(secondline)

# always close the file, don't leave it open
f.close