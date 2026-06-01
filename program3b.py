
#list operations

n = int(input("Enter the number of elements of the list: "))

L = []

for i in range(n):
	value = int(input("Enter the element: "))
	L.append(value)

print("Initial list: ", L)

#Inserting an element

print("---Inserting an element---")

pos = int(input("Enter the position of the element to enter: "))
val = int(input("Enter the value to enter: "))
L.insert(pos, val)

print("After insertion: ", L)

#Appending an element

print("---Appending an element---")

val = int(input("Enter the value to append: "))
L.append(val)

print("After appending: ", L)

#Removing an element

print("---Removing an element---")

val = int(input("Enter the value to remove: "))
L.remove(val)

print("After removing: ", L)

#Popping an element

print("---Popping an element---")

popped = L.pop()
print("Popped element: ", popped)

print("After popping: ", L)

#Displaying the list

print("---Displaying the element---")

print(L)


#Clearing the list

print("---Clearing the list---")

L.clear()
print("After clearing the list: ", L)
