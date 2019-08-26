# 判断质数

num = int(input('请输入一个数：'))

if num > 1:
	for x in range(2,num):
		if num % x == 0:
			print(str(num) + '不是质数')
			print(x,"乘于",num//x,"是",num)
			break
	else:
		print(str(num) + '是质数')
else:
	print('输入的数字必须大于 1')

# 求一定范围内的质数
lower = int(input('请输入区间最小的值'))
upper = int(input('请输入区间最大的值'))

for i in range(lower,upper + 1):
	if i > 1:
		for x in range(2, i):
			if i % x == 0:
				break
		else:
			print(str(i) + '是质数')
	else:
		print('输入的数字必须大于 1')