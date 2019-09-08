# 计算字典的和
def myDict(dicts):
	sum = 0
	for i in dicts:
		sum = sum + dicts[i]

	return sum


dicts = {'a': 100, 'b': 1 }

print(myDict(dicts))

# 移除没有的 key 会报错
del dicts['a']

print(dicts)
# 使用 pop() 移除没有的 key 不会发生异常
dicts.pop('b')
print(dicts)
