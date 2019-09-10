import time
import datetime
# print('按下回车开始计时，按下 Ctrl + C 停止计时。')

# while True:
# 	try:
# 		input()
# 		startTime = time.time()
# 		print('开始')
# 		while True:
# 			print('计时：', round(time.time() - startTime, 0), '秒', end='\n')
# 			time.sleep(1)
# 	except KeyboardInterrupt:
# 		print('结束')
# 		endTime = time.time()
# 		print('总共时间为：', round(endTime - startTime, 2), 'secs')

# 将字符串的时间转换为时间戳
time1 = "2019-5-10 23:40:00";

# 先转换为时间数组
timeArr = time.strptime(time1, '%Y-%m-%d %H:%M:%S')

# 转换为时间戳
timeStamp = int(time.mktime(timeArr))
print(timeStamp)

# 先获得时间数组格式的日期
threeDayago = (datetime.datetime.now() - datetime.timedelta(days = 3))

# 转换为时间戳
timeStamp2 = int(time.mktime(threeDayago.timetuple()))
styleTime = threeDayago.strftime('%Y-%m-%d %H:%M:%S')
print(styleTime)


now = int(time.time())
timeArr2 = time.localtime(now)
styleTime2 = time.strftime('%Y-%m-%d %H:%M:%S', timeArr2)
print(styleTime2)





