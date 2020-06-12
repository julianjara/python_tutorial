#this program will append names to a list until user types 'quit'
# start with an empty list
names = []

#set name to something different from quit, this is to guarantee the while loops 
new_name = ''

while new_name != 'quit':
    new_name = input("Enter new name or 'quit'")
    if new_name == 'quit':
        break
    names.append(new_name)

print(names)