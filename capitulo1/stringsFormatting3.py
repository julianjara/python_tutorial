# another way to manipulate strings is by using the format() method
# “string to be formatted” and use {} 
brand = 'Apple'
exchangeRate = 0.65667788

message = 'The price of this {0:s} laptop is {1:d} AUD and the exchange rate is {2:4.2f} AUD to 1 USD'.format(brand, 1299, exchangeRate)
print (message)

#another way is with no formatting at all
message = 'The price of this {} laptop is {} AUD and the exchange rate is {} AUD to 1 USD'.format(brand, 1299, exchangeRate)
print (message)