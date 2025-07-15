def divide_nums(a, b):
	if b == 0:
		raise ValueError("Second argument cant't be 0")
	return a / b

try:
	divide_nums(10, 0)
except ValueError as e:
	print(e)