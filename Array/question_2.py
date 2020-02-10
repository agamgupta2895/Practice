# Given an Array find an element which occurs more than n/2 times


size = int(input("Number of elements in an array"))

arr = {}

for i in range(0, size):
    elements = int(input("Enter the number"))
    if elements in arr:
        arr[elements] = arr[elements] + 1
        if arr[elements] > size/2:
            print("Moore number : " , elements)
            break
    else:
        arr[elements] = 1

print(arr)