#this program will sum values until 'n'

sum = 0
i = 0
n = int(input("entra el valor the n"))

while i <= n:
    print("i va en =", i)
    sum += i
    print("la sumatoria va en:",sum)
    i += 1
    
print("la suma total es =",sum)
