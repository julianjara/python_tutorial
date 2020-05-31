# another way to manipulate strings is by using the % operator
# “string to be formatted” %(values or variables to be insterted into string, separated by commas)
brand = 'Apple'
exchangeRate = 0.65667788

message = 'The price of this %s laptop is %d AUD and the exchange rate is %4.2f AUD to 1 USD' % (brand, 1299, exchangeRate)
print (message)