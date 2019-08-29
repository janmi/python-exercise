# 获取指定月份天数

import calendar

mm = int(input('请输入要查询的月份：'))

list = calendar.mdays # 返回一个列表，列表的第一项为 0 

print(list[mm])