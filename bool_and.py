for b in (False, 0, 0.0, '', {}, []):
	print(b, end='\t')
	print(b and sdf, end='\t')
	print((b and sdf) is b)
