# 最大公约数

def hcf(x, y):
	if x > y:
		val = x
	else:
		val = y
	for i in range(1, val + 1):
		if (x % i == 0) and (y % i == 0):
			val = i

	return val

	
# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
 
print( num1,"和", num2,"的最大公约数为", hcf(num1, num2))