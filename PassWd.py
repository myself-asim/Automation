import string
from random import randrange

alpha = string.ascii_letters
sym = "!@#$%^&*()_+"

def passWdGenerator(symbol, num, string):

	passWd = string + symbol + num 

	print(passWd)


num = randrange(75)
num += randrange(95)
num = str(num)

symbols = sym[randrange(10)]
symbols += sym[randrange(10)]

string = ""
for i in range(0, 8):

	string += alpha[randrange(50)]


passWdGenerator(symbols, num, string)
