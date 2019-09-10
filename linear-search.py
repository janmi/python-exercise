def linearSearch(arr, target):
	for i in range(len(arr)):
		if arr[i] == target:
			return i

	return -1

arr = [ 'A', 'B', 'C', 'D', 'E' ]; 
target = 'D'; 

print(linearSearch(arr, target))