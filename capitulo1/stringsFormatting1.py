# ejemplo de manipulación de 'Strings' con funciones predefinidas
# para un lista completa the funciones 'https://www.w3schools.com/python/python_ref_string.asp'

txt = "hello, I LOVE apples, red apple and green apple"
print(txt)

x = txt.capitalize()
print (x)  #prints txt with the first letter capitalized

x = txt.count("apple")
print(x)   # prints the number of times apple is found

x = txt.isnumeric()
print(x)   #returns True if txt is all numeric

x = txt.istitle()
print(x)   #returns True if txt follows the rules of a title

x = txt.isalpha()
print(x)   #returns if all characters in the string are in the alphabet

x = txt.lower()
print(x)  #Converts a string into lower case

x = txt.rindex("LOVE") 
print(x)  #Searches the string for a specified value and returns the last position of where it was found

x = txt.swapcase()
print(x)  #Swaps cases, lower case becomes upper case and vice versa