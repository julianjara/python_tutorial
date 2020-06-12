# use a for loop to read a file
f = open('text.txt', 'r')

for line in f:
    print (line, end = '')

f.close