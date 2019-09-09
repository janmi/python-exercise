# 合并字典
def Merge(dict1, dict2):
	return (dict1.update(dict2))

dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 

Merge(dict1, dict2)
# dict1 合并了 dict2
print(dict1)

# 使用 **，函数将参数以字典的形式导入
def Merge2(dict1, dict2):
	res = {**dict1, **dict2}
	return res

dict3 = {'a': 10, 'b': 8} 
dict4 = {'d': 6, 'c': 4} 

print(Merge2(dict3, dict4))


