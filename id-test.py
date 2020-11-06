import sys
a = list(range(10))

for x in a:
	print(id(x), sys.getsizeof(x))
	