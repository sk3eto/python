
#Raising errors

def DivExp(a, b):
	
	try:
		assert a > 0, "Error: 'a' must be greater than 0"
		c = a / b
		return c
	except AssertionError as e:
		print(e)
	except ZeroDivisionError:
		print("Cannot divide by 0")
		return None

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

result = DivExp(n1, n2)
if result is not None:
	print("Result of a / b: ", result)
