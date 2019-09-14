# Python 迭代器
str1 = 'liangdianshui'
iter1 = iter ( str1 )

for i in iter1:
	print(i)

print('=======')

while True:
	try:
		print(next(iter1))
	except StopIteration:
		break

