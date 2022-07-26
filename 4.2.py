def trypal(num):
	num = str(num)
	if num[0:len(num)//2] == num[len(num)//2:len(num)]:return True
	return False


numbers = []
i = 999
while i > 100:
	for j in range(100, i):
		num = i * j
		if trypal(num):numbers.append(num)
	i -= 1
	
print(max(numbers))