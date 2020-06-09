# this function will multiply a number by 2, and so on

def multplier(limit):
	respuesta = 1
	for x in range(1,limit):
		print(respuesta)
		respuesta = respuesta*2
	return respuesta

num = int(input("hasta cuanto quieres multiplicar?:"))

valor = multplier(num)
print(valor)