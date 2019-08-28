# 最大功倍数

def lcm(x, y):
	if x > y:
		val = x
	else:
		val = y

	while True:
		if (val % x) == 0 and (val % y == 0):
			lcm = val
			break
		val += 1
	return val


num1 = int(input('请输入第一个数：'))
num2 = int(input('请输入第二个数：'))

print(lcm(num1, num2))