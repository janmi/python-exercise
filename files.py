# 文件操作

# 写文件
with open('test.txt', 'wt') as out_file:
	out_file.write('写入文件操作')

# 读取文件
with open('test.txt', 'rt') as in_file:
	text = in_file.read()

print(text)