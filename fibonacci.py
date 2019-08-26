# 斐波那契数列
num = int(input('请输入一个数字：'))
fibonacci = [0, 1]

if num < 1:
	print('数字必须大于1')
else:
	for x in range(1, num):
		fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)