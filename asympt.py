from math import factorial as f
n = 20
for i in range(n):
	print(i, end='\t')
	print(i*i, end='\t')
	print(2**i, end='\t')
	print(f(i))
	