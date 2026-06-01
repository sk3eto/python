
a = float("Enter the first number: ")
b = float("Enter the second number: ")

choice = int(input("Enter choice: "))

print("\n1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

if choice == 1:
	print("Add: ", a + b)
elif choice == 2:
	print("Subtract: ", a - b)
elif choice == 3:
	print("Multiply: ", a * b)
elif choice == 4:
	print("Divide: ", a / b)
else:
	print("Invalid option")

