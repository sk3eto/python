
#Fibonacci sequence

n = int(input("Enter the value of n: "))

first_num = 0
second_num = 1

print("The fibonacci series is: ")
print(first_num)
print(second_num)

for i in range(2, n):
	new_num = first_num + second_num
	print(new_num)

	first_num = second_num
	second_num = new_num


