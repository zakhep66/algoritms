import time

amount = int(input('количесmво элементов: '))
file = open('../генератор/' + str(amount) + ".txt", "r")
arr = (file.read()).split(' ')

for i in range(len(arr)):
    arr[i] = int(arr[i])  # Перевод массива строк в массив чисел

start_time = time.time()


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


heapSort(arr)

print("--- %s seconds ---" % (time.time() - start_time))

my_file = open("sort_heap{}.txt".format(amount), "w")
for i in range(0, amount):
    my_file.write(str(arr[i]) + " ")
my_file.close
