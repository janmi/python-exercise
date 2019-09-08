# 翻转第一和最后一个元素
def swapList(list):
	list[0], list[-1] = list[-1], list[0]
	return list

arr = [1,2,3]

print(swapList(arr))
# 翻转指定元素
def swapPositions(list, pos1, pos2):
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list

arr2 = [1,2,3,4,5,6]
print(swapPositions(arr2, 3, 5))
# 翻转列表
def Reverse(list):
	list.reverse()
	return list

print(Reverse(arr2))

# 判断列表是否存在指定元素

if 4 in arr2:
	print('存在这个元素')

# 清空列表

arr2.clear()

print(arr2)

# 测试是否指向同一个内存
arr3 = [7,8,9]
arr4 = arr3

arr3.pop()
print(arr4)

# clone 列表
def clone(list):
	cloneList =  list[:]
	return cloneList

list2 = [1,2,3,4]
list3 = clone(list2)
list2.append(5)
print(list2)
print(list3)

def clone2(list):
	cloneList = [] + list
	return cloneList

print(clone2(list2))

# 计算一个元素在列表中出现的次数

def Count(list, x):
	conut = 0
	for i in range(len(list)):
		if x == list[i]:
			conut += 1
	return conut

list4 = [15, 6, 7, 10, 12, 20, 10, 28, 10]

print(Count(list4, 10))

# 使用列表内置的计数方法
print(list4.count(10))

# 计算列表乘积
def multiplyList(list): 
	result = 1
	for i in range(len(list)):
		result = result * list[i]

	return result

print(multiplyList([1,2,3]))

# 查找列表中最小\大元素

list5 = [4,6,3,8]

print(min(list5))
print(max(list5))

list5.sort()

print(list5[0])
















