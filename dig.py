import sys
sys.setrecursionlimit(1000000)

def getsum(n):
	if n==1:
		return 1
	else:
		return n+getsum(n-1)

print(getsum(100000))

