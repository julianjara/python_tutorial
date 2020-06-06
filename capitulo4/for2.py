# you can use the break statement to break out of a for
print("example1")
fruits = ["apple", "banana", "cherry", "orange", "lemon", "pear", "pineapple", "strawberry"]
for x in fruits:
    print(x)
    if x == "pear":
        break 
print("example2")        
print("now with the break before the print, it should exclude the fruit the meets the criteria of break")
for x in fruits:
    if x == "pear":
        break
    print(x)
print("example3")
print("do not print pear")
for x in fruits:
    if x == "pear":
        continue
    print(x)
