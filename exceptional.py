def convert(str):
	try:
		x = int(str)
	except (ValueError, TypeError) as e:
		print(e)
		x = -1
	return x
	
print(convert('10'))
print(convert('SHE'))
print(convert([1,2,3,4]))
print(convert('123'))