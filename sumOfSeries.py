# 求N个数的立方和

def sumOfSeries(n):
	sum = 0
	for x in range(1, n+1):
		sum += x*x*x
	return sum


print(sumOfSeries(5)) 