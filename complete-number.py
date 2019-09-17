# 求完全数

def completeNumber(num):
	list = ''
	for i in range(1, num):
		sum = 0
		for x in range(1, i):
			if i % x == 0:
				if x != i:
					sum = sum + x
		if sum == i:
			list += ' ' + str(sum)
	return list

print(completeNumber(10000))

