import math
def is_square(number):
	if(number < 0):
		return False
	if(number == 0):
		return True
	if(number == 1):
		return True
	sqr_number = math.sqrt(number)
	non_decimal = sqr_number % 1 == 0
	if(non_decimal == True):
		square = (number/sqr_number == sqr_number)
		if(square == True):
			return True
		else:
			return False
 
