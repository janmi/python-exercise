import random

for num in range(0,3):
	print('明天就要放假了！')
	if num == 2:
		print('重要的事情说三遍！')

str = '明天就要放假了！\n'
str_end = '重要的事情说三遍！'
print(str*3 + str_end)

编程计算原价和折扣价
price = 300
hoodie = price
pants = price
print("卫衣的原价是"+str(hoodie)+"元。")
print("运动裤的原价是"+str(pants)+"元。")
hoodie = hoodie * 0.5
pants = pants * 0.8
print("卫衣的\"双11价\"是"+str(hoodie)+"元。")
print("运动裤的\"双11价\"是"+str(pants)+"元。")
sum = 0
for num in range(0,101):
		sum = sum + num
print(sum)

names = ['哈利','罗恩','赫敏','纳威']
for name in names:
	print(name + '通过了等级考试')

def weiboUser(X,Y):
	if X > 20 or Y > 10:
		print('非常活跃用户')
	elif 10 <= X < 20 or 5<= Y < 10:
		print('活跃用户')
	elif X < 3 and Y <=1:
		print('消极用户')
	else:
		print('普通用户')

weiboUser(10,10)

string = "The high-profile engagement between Chinese President Xi Jinping and his U.S. counterpart Donald Trump on Thursday has caught the spotlight globally. Experts said their meeting has borne remarkable fruit, and the forward-looking attitude of the two heads of state towards bilateral cooperation will bring benefits to the two countries, the Asia-Pacific and the world at large."
words = string.split(' ')
index = string.find('Trump')

if index > -1:
		print('This article maybe about Trump')
else:
		print('This article maybe not about Trump')

print(index)


data = {
  '芳华' : ['黄轩','苗苗'],
  '战狼2' : ['吴京','吴刚','卢婧姗'],
  '无问西东' : ['章子怡','黄晓明','张震','王力宏'],
  '大兵小将' : ['成龙', '王力宏', '刘承俊']
}

def movie(name):
	for mov in data:
		if name in data[mov]:
			print(name + '出演了电影' + mov)
		# for item in data[mov]:
		# 	if name == item:
		# 		print(name + '出演了电影' + mov)

movie('成龙')

def movie2():
	for item in data:
		print('电影《'+ item +'》的主演有' + '、'.join(data[item]) + '。')

movie2()


def order(num):
	if num > 3:
		return '总计：' + str(5*num) + '元'
	else:
		return '总计：' + str(6*num) + '元'

sum = order(4)
print(sum)

list = [22, 23, 20, 19, 21, 22, 22, 23, 24, 20, 20, 22]

def attendance():
	count = 0
	for item in list:
		if item < 20:
			count = count + 1
	return count
print(attendance())

print(random.randint(1, 6))


movies = ['碟中谍', '泰坦尼克号', '荒野猎人', '卧虎藏龙', '色戒', '借东西的小人艾利特']
def oscar():
	for index in range(len(movies)):
		if movies[index] == '泰坦尼克号':
			movies[index] = '*泰坦尼克号'

oscar()
print(movies)

string = "哈利、罗恩、赫敏"
arr = string.split('、')
print(arr)

list = [1,2,3,4,5,6,7,8,9]
for index in range(len(list)):
	list[index] = list[index] + 100
	if 2<= index <=5:
		print(list[index])
print(list[-1])

string = "哈利·波特、罗恩·韦斯莱、赫敏·格兰杰、乔治·韦斯莱、弗雷·韦斯莱、纳威、卢娜、阿不思·珀西瓦尔·邓布立多"
names = string.split('、')
reslt = []
for name in names:
	if '·' in name:
		reslt.append(name.split('·')[-1])
print(reslt)

# 返回当前执行的目录
import os
print(os.getcwd()) 

# 返回path指定的文件夹包含的文件或文件夹的名字的列表。
print(os.listdir(os.getcwd()))

# 创建文件夹
# os.mkdir('test')

# 逐级创建文件夹
# os.makedirs('test2/child/item')

# 递归删除文件夹
# os.removedirs('test2/child/item')
# 修改文件名
# os.rename('test', 'test3')

print(os.stat('test3'))

class MyClass():
	num = 120
	def sum(self, a, b):
			return a + b
	def str(self):
		return 'sss'


x = MyClass()

print(x.num)
print(x.sum(1, 2))
print(x.str())


# # 用户输入数字
# num1 = input('输入第一个数字：')
# num2 = input('输入第二个数字：')
 
# # 求和
# sum = float(num1) + float(num2)
 
# # 显示计算结果
# print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))

# num3 = input('输入一个数字')
# print(num3)

print(random.randint(0,9))

# 交换变量值

# x = input('输入 x 值: ')
# y = input('输入 y 值: ')
 
# # 不使用临时变量
# x,y = y,x

# print(x,y)

num4 = float(input('输入一个数字：'))

if num4 > 0:
	print('是正整数')
elif num4 == 0:
	print('是零')
else:
	print('是负数')

# Python 判断字符串是否为数字
num5 = input('输入一个数字：')
print(num5.isdigit())


num6 = float(input('输入一个数字：'))
if num6 % 2 == 0:
	print('是偶数')
else:
	print('是奇数')

year = float(input('输入一个年份：'))

if (year % 4) == 0:
	if (year % 100) == 0:
		if (year % 400) == 0:
			print(str(int(year)) + '是闰年')
		else:
			print('是平年')
	else:
		print('是平年')
else:		
	print('是平年')











