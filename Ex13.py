 arr = [25, 11, 7, 75, 56]
 max = arr[0];
 for i in range(0, len(arr)):
	if(arr[i] > max):
		max = arr[i];
		print("The maximum number present in the given array is: " + str(max));
