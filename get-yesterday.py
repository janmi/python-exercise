# 获取昨天的日期

import datetime

def getYesterday():
	yesterday = datetime.date.today() + datetime.timedelta(-1)
	return yesterday

print(getYesterday())