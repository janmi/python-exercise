# Python ASCII码与字符相互转换
string = input('请输入一个字符：')

ascllCode = int(input('请输入一个ASCll码：'))

print(string + '的ASCll码为：', ord(string))
print(str(ascllCode) + '对应的字符为：', chr(ascllCode))