import sys
x = sys.maxsize
x = 2147483647
sys.setrecursionlimit(x)
def dg(x):
	x = x - 1
	if x == 0 :
		return
	else :
		print(x)
		dg(x)

x = 900
dg(x)

x = sys.maxsize

x = type(x)
print(sys.maxsize)
print(x)