def f(*args):
	if not args:
		print('no')
	else:
		for arg in args:
			print(arg * 2)


f()
f(0)
f(1, 2, 's')
