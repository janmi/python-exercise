# 阶乘
for i in range(1,10):
	for j in range(1, i+1):
		print('{}x{}={}\t'.format(j, i, j*i), end='')
	print('\n')



print('\n')

print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))