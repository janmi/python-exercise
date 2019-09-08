# 删除指定位置字符串

str = 'joyanmi'
num = int(input('输入要删除的位置：'))
print(str.replace(str[num], '', 1))

# 判断字符串中是否包含子字符串

if str.find('joy') > -1:
	print('包含')
else: 
	print('不包含')

# 字符串长度

print(len(str))


# 用正则提取字符串中的 url
import re # 引入正则库
str2 = ' 可以访问我个人的官网的网址有 http://www.joy.com 或者 https://www.joy.com'

urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', str2)
print(urls)

# 将字符串作为代码执行

def execCode(str):
	exec(str)

execCode('print(12345)')

# 字符串翻转

# 使用字符串切片

str3 = 'janmi'
print(str3[::-1])

# 使用内置翻转函数 reversed

print(''.join(reversed(str3)))
