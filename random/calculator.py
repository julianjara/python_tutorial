# this is a calculator
# first define all the functions for all the mathematic operations
def suma(x, y):
    return x + y
def resta(x, y):
    return x - y
def multiplicacion(x, y):
    return x * y
def division(x, y):
    return x / y

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("x. EXIT")

choice = 1
while choice != 'x':
    # take input from the user
    choice = input("escoja la operacion: ")

    # check if option is 1,2,3 or 4
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("escriba un numero:"))
        num2 = float(input("escriba otro numero:"))

        if choice == '1':
            print(num1, "+", num2, "=", suma(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", resta(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplicacion(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
    
    elif choice == 'x':
        print("Bye Bye")
        # input == False
        #break

    else:
        print("ERROR - mala opcion")
