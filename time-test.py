import time

print('按下回车开始计时，按下 Ctrl + C 停止计时。')

while True:
	try:
		input()
		startTime = time.time()
		print('开始')
		while True:
			print('计时：', round(time.time() - startTime, 0), '秒', end='\n')
			time.sleep(1)
	except KeyboardInterrupt:
		print('结束')
		endTime = time.time()
		print('总共时间为：', round(endTime - startTime, 2), 'secs')