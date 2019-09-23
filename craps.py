# craps赌博游戏
import random

def recursiveCraps(firstSum, num):
	x = random.randint(1,6)
	y = random.randint(1,6)
	sum = x + y

	num += 1
	if sum == firstSum:
		print('第' + str(num)+ '次摇塞子点数是'+ str(sum) +'和第一次摇塞子点数'+ str(firstSum) +'一样,玩家胜')
	elif sum == 7:
		print('第' + str(num)+ '次摇塞子点数是'+ str(sum) +',庄家胜')
	else:
	 recursiveCraps(firstSum, num)

def craps(recursiveSum):
	x = random.randint(1,6)
	y = random.randint(1,6)
	sum = x + y
	if sum == 7 or sum == 11:
		print('第一次摇塞子点数是'+ str(sum) +',玩家胜')
	elif sum == 2 or sum == 3 or sum == 12:
		print('第一次摇塞子点数是'+ str(sum) +',庄家胜')
	else:
		recursiveCraps(sum, 1)

craps(0)
	