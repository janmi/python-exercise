# 求百钱百鸡
def HundredsOfChickens():
	list = []
	for x in range(1, 100):
		for y in range(1, 100):
			z = (100 - x - y)
			if (9 * x) + (15 * y) + z == 300:
				list.append([x,y,z])
	
	return list

print(HundredsOfChickens())