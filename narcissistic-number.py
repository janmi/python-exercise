# 求水仙花数 水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。 https://baike.baidu.com/item/%E6%B0%B4%E4%BB%99%E8%8A%B1%E6%95%B0
def isNarcissisticNumber(num):
	numStr = str(num)
	if len(numStr) != 3:
		print(str(num) + '不是水仙花数')

	numSum = pow(int(numStr[0]),3) + pow(int(numStr[1]), 3) + pow(int(numStr[2]), 3)

	if (numSum == num):
		print(str(num) + '是水仙花数')
	else:
		print(str(num) + '不是水仙花数')

	# return True


isNarcissisticNumber(153)
	