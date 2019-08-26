# 阶乘

factorial = int(input('输入一个阶乘数字'))

if factorial < 0:
	print('数字必须大于0')
elif factorial == 0:
	print('0的阶乘是1')
else:
	for x in range(1, factorial):
		factorial = factorial * x
print(factorial)
