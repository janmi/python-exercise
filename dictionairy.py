# 字典排序
def dictionairy():
	keyValue = {}
	keyValue[2] = 345
	keyValue[1] = 12
	keyValue[5] = 45
	keyValue[4] = 789
	keyValue[3] = 1

	# sorted(key_value) 返回一个迭代器
	# 字典按键排序
	for item in sorted(keyValue):
		print((item, keyValue[item]), end=' ')

dictionairy()
print('\n')
# 按值排序

def dictionairy2():
	keyValue = {}
	keyValue[2] = 345
	keyValue[1] = 12
	keyValue[5] = 45
	keyValue[4] = 789
	keyValue[3] = 1

	print(sorted(keyValue.items(), key = lambda kv:(kv[1], kv[0])))

def main():
	dictionairy2()

if __name__ == '__main__':
	main()

# 字典列表排序
lis = [{ "name" : "Taobao", "age" : 100},  
{ "name" : "Runoob", "age" : 7 }, 
{ "name" : "Google", "age" : 100 }, 
{ "name" : "Wiki" , "age" : 200 }]


# 通过 age 升序排序

print(sorted(lis, key = lambda i: i['age']))

print ("\r") 
  
# 先按 age 排序，再按 name 排序
print(sorted(lis, key = lambda i: (i['age'], ['name'])))

# 按 age 降序排序; reverse 值默认为False按照升序排序，设置为 True 则降序排序
print(sorted(lis, key = lambda i: i['age'], reverse = True))


