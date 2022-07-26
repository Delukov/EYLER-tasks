from random import randint
import math

# def simplecheck(num):

# 	for i in range(2, (num//4)):
# 		if ((math.pow((i * randint(1,4)),num) // num) != (i * randint(1,4) // num)):
# 			return False

# 	return True
def simpleiter(num):
	for i in reversed(range(2, round(num ** (0.5)))):
		if (num % i) == 0: 
			return False
	return True

# def trydiv(num):
# 	for i in reversed(range(2, (num//2)+1)):
# 		if simpleiter(i) and (num % i == 0):
# 			return i
# 	return 1

def trydiv(num):
	num1 = round(num ** (0.5))
	if num % 2 == 0:
		for i in reversed(range(1, (num1 - 1), 2)):
			print(i)
			if (num % i == 0):
				if simpleiter(i):
					return i
	else:
		for i in reversed(range(1, num1, 2)):
			print(i)
			if (num % i == 0):
				if simpleiter(i):
					return i

#print(simpleiter(13))
print(trydiv(6857))