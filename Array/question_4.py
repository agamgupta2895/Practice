# Find the element in array which occurs odd number of times rest occurs even number of times

size = int(input("Number of elements in an array"))

arr = []

for i in range(0, size):
    elements = int(input("Enter the number"))
    arr.append(elements)

num = 0
for i in arr:
    num = num ^ i

print("XOR number - ", num)


