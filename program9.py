
#Complex numbers

class complex:
	def __init__(self, real, imaginary):
		self.real = real
		self.imaginary = imaginary
	def __add__(self, other):
		return complex(self.real + other.real, self.imaginary, other.imaginary)
	def __str__(self):
		return f"{self.real} + {self.imaginary}"

def read(n):
	complex_number = []
	for i in range(n):
		real = float(input(f"Enter the real part of the complex number {i + 1}: "))
		imaginary = float(input("Enter the imaginary part of the complex number: "))
		complex_number.append(complex(real, imaginary))
	return complex_number

def sum(complex_number):
	total = complex(0, 0)
	for cn in complex_number:
		total = total + cn
	return total

n = int(input("Enter the number of complex number (N >= 2): "))

if n < 2:
	print("N must be at least 2")
	exit()

complex_number = read(n)
total = sum(complex_number)
print("The sum of the complex number is: ", total)
