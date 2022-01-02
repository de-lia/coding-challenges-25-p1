def isPrime(h):
	h = int(h)
	test = None
	for x in range(2, h):
		if (h%x) == 0:
			test = False
			print(f"{test}, the number {h} is not prime!")
			break
		else:
			test = True
			print(f"{test}ly, the number {h} is a prime!")
			break
>>> isPrime(input("Enter a number.\n"))
