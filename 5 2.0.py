def divcheck(num):
	if (num%20 == 0) and (num%19 == 0) and (num%17 == 0) and (num%18 == 0) and (num%16 == 0) and (num%15 == 0) and (num%14 == 0) and (num%13 == 0) and (num%12 == 0) and (num%11 == 0): return True
	return False


i = 20

while divcheck(i) == False:
	i += 20

print(i)
	
