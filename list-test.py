list = [1,2,3,4,'5','6']

print(list[1:3])
list.append(7)
print(list)
list.insert(7, '8')
print(list)
list.extend(['9', 10])
print(list)

print(list.index(10))

print('9' in list)

# 删除一个元素, 如果元素不存在，会引发一个异常
list.remove(10) 
print(list)
# 删除最后一个元素，并返回一个元素
list.pop()
print(list)

# 列表运算符

list = list + ['9', '10']
print(list)
list += [11]
print(list)

# * 号并不是相乘，而是每个元素在列表中增加多 n 个
newlist = [1, 2] * 2

print(newlist) # 打印出 [1,2,1,2]

# 使用 join 拼接 list， join 只能拼接 list 是字符串的数据，数据类型不对会抛出异常
newStr = '-'.join(['my', 'name', 'is', 'joy'])
print(newStr)

# 分割字符串
newlist2 = newStr.split('-')
print(newlist2)

# list 的映射解析
list3 = [2, 8, 10]
print([item * 2 for item in list3])

# list 过滤

print([item for item in list3 if item > 2])





