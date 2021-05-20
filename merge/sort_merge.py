import time
start_time = time.time()

amount = 10
file = open("db"+str(amount)+".txt")
arr=(file.read()).split(' ')
# print(arr)


def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
 
        mergeSort(left)
        mergeSort(right)
 
        i = 0
        j = 0
        k = 0
 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

mergeSort(arr)

print("--- %s seconds ---" % (time.time() - start_time))

# print(arr)

my_file = open("sort_merge{}.txt".format(amount), "w")
for i in range(0,amount):
    my_file.write(str(arr[i])+" ")
my_file.close