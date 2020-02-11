# Find the maximum difference bw two elements in an array such that the larger element appears after the smaller element

size = int(input("Number of elements in an array"))

arr = []

for i in range(0, size):
    elements = int(input("Enter the number"))
    arr.append(elements)

min_num = arr[0]
max_diff = 0
for i in arr:
    if i < min_num:
        min_num = i
    if i - min_num > max_diff:
        max_diff = i - min_num


print("Max diff : " , max_diff)