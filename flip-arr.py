def leftRotate(arr, n, d):
	for x in range(d):
		leftRotatebyOne(arr, n)
		
def leftRotatebyOne(arr, n):
	temp = arr[0]
	for i in range(n-1):
		arr[i] = arr[i+1]
	arr[n-1] = temp

arr = [1,2,3,4,5,6,7]

leftRotate(arr, 7, 3)

for x in range(len(arr)):
	print(arr[x])