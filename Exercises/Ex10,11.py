arr = [60, 80, 50, 10]
sumArr = 0
avgArr = 0
for i in range(0, len(arr)):
	sumArr += arr[i]

	
avgArr = sumArr/len(arr)
print("The Sum is: ", sumArr)
print("The sum and average respectively are: ", sumArr, "and", avgArr)
