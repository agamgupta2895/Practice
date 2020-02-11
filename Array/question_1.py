# In an array find a pair with the sum X

size = int(input("Number of elements in an array"))

arr = {}


l = []
for i in range(0, size):
    elements = int(input("Enter the number"))
    l.append(elements)
    arr[elements] = 0

sum = int(input("Sum of the number "))

print(arr)

for element in l:
    firstNum = element
    secondNum = sum - firstNum
    if secondNum in arr and arr[secondNum] == 1:
        print("Pair = ", firstNum, secondNum)
    else:
        arr[firstNum] = 1
