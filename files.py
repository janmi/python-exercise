# 文件操作
import time
import json


# 写文件
with open('test.txt', 'wt') as out_file:
	out_file.write('写入文件操作')

# 读取文件
with open('test.txt', 'rt') as in_file:
	text = in_file.read()

print(text)


# open 函数再指定文件不存在或者无法打开的时候会引发一场状况导致程序崩溃

def main():
	f = None
	try:
		f = open('test.txt', 'r', encoding='utf-8')
		print(f.read())
	except FileNotFoundError:
		print('无法打开指定的文件')
	except LookupError:
		print('指定了位置的编码')
	except UnicodeDecodeError:
		print('读取文件编码时出错')
	finally:
		if f:
			f.close()


def main2():
	# 通过for-in循环逐行读取
	with open('test.txt', mode='r') as f:
		for line in f:
			print(line, end='')
			time.sleep(0.5)

	# 读取文件按行读取到列表中
	print('')
	with open('test.txt') as f:
		lines = f.readlines()
		print(lines)


# json模块主要有四个比较重要的函数，分别是：

# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象
def main3():
	mydict = {
	    'name': '骆昊',
	    'age': 38,
	    'qq': 957658,
	    'friends': ['王大锤', '白元芳'],
	    'cars': [
		      {'brand': 'BYD', 'max_speed': 180},
		      {'brand': 'Audi', 'max_speed': 280},
		      {'brand': 'Benz', 'max_speed': 320}
	    ]
	}
	try:
  	  with open('data.json', 'w', encoding='utf-8') as fs:
  				json.dump(mydict, fs)
	except IOError as e:
  		print(e)
	print('数据保存完成')

if __name__ == '__main__':
	main()
	main2()
	main3()