import random



file = open("sort_buble1000.txt")
arr=(file.read()).split(' ')
# print(arr)
# искомое число
value = int(input())

mid = len(arr) // 2
low = 0
high = len(arr) - 1

while int(arr[mid]) != value and low <= high:
    if value > int(arr[mid]):
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID =", mid)