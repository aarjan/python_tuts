def fib(n):
	x,y = 0,1
	while y < n:
		print(y,end=' ')
		x,y = y,x+y
	print()

def fib2(n):
	result = []
	x,y = 0,1
	while y < n:
		result.append(y)
		x,y = y,x+y
	return result

if __name__ == "__main__":
    import sys
    fib2(int(sys.argv[1]))
