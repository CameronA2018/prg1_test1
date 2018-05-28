
def is_factorion(n):
	if(n == 2):
		return True
	def find_digits(n):
		str_n = str(n)
		digits = []
		x = 0
		while(x<len(str_n)):
			digit = str_n[x]
			digits.append(digit)
			x += 1
		return (digits)
	diges = find_digits(n)
	def find_factors(diges):
		x = 0
		spots = []
		sums = []
		while(x<len(diges)):
			spot = diges[x]
			spots.append(spot)
			y = int(spots[x])
			sum = 0
			while(y>0):
				sum = sum + y
				y -= 1
			sums.append(sum)
			x += 1
		return (sums)
	summarion = find_factors(diges)
	def find_if_factorian(summarion):
		x = 0
		total = 0
		while(x<len(summarion)):
			total = summarion[x] + total
			x += 1
		if(total == n):
			return True
	if(find_if_factorian(summarion) == True):
		return True
	else:
		return False