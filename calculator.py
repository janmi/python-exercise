# 简单计算器实现

# 定义函数
# 加法
def add(a, b):
 	return a + b

# 减法
def subtract(a, b):
	return a - b

# 相乘
def multiply(a, b):
	return a * b

# 相除

def divide(a, b):
	return a / b


# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
 
choice = input("输入你的选择(1/2/3/4):")

num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

if choice == '1':
	print(add(num1, num2))
elif choice == '2':
	print(subtract(num1, num2))
elif choice == '3':
	print(multiply(num1, num2))
elif choice == '4':
	print(divide(num1, num2))


