l = [[f'{x*y:3}' for x in range(1, 11)] for y in range(1, 11)]
for s in l:
	print(*s)
