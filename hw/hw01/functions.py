from operator import add
def square(x):
	"""cauculate the square of x

	x -- abrtry number
	"""
	return pow(x,2)

def sum_square(x,y):
	"""cauculate the sum of square x and square y
	
	x, y -- abratry numbers
	"""
	return add(square(x),square(y))

def print_none():
	"""print none"""
    if not None:
        print("none is a false boolean context")

