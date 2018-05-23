def cycle(n):
	strn = str(n)
	sum = 0
	for sdigit in str(n):
		digit = int(sdigit)
		sum = sum + (digit * digit)
	return sum

def is_happy(n):
	''' Extra credit
	A happy number is a number defined by the following process: Starting with any positive integer,
	replace the number by the sum of the squares of its digits,
	and repeat the process until the number equals 1 (where it will stay), 
	or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

	Write a function that tells you if n is a happy number
'''
	found = []
	while(n != 1):
		n = cycle(n)
		if(n in found):
			return False
		found.append(n)
	return True 