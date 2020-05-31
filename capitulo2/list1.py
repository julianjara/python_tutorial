# the following list contains the age of people
list=[24, 23, 27, 40, 12, 60, 30]
#now we print any of the ages using the position index
print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[6])

# I can list using a reverse order where -1 is the last one and -2 the second last and so on
print("now printing the last two of the list using -1 and -2 indexes")
print(list[-1])
print(list[-2])

# we can also assign a list to a variable
# ages = list 
ages = list
print(ages)

# now we can create another list with a subset of the original with the slice notation
# ages3 = list[2:4]
# which adds index 2 and 4-1, so 27 and 40
ages3 = list[2:4]   # this notation is called slice where the item at the start is included but not the last
                    # so if you want to include both you have to do [2:4] 
print(ages3)
ages3 = list[2:3]  # this explains how index 3 is not shown, to show it you have to do [2:4]
print(ages3)
#
# the slice notation includes a third number known as stepper
# ages4 = list[1:5:2] nos da del index 1 al 5-1 en saltos de a 2
ages4 = list[1:6:2]
print(ages4)