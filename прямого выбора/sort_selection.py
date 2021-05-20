import time
start_time = time.time()

amount = int(input('количество элементов: '))
file = open('../генератор/' + (str(amount))+".txt", "r")
arr=(file.read()).split(' ')

for i in range(len(arr) - 1):
    m = i
    j = i + 1
    while j < len(arr):
        if int(arr[j]) < int(arr[m]):
            m = j
        j = j + 1
    arr[i], arr[m] = arr[m], arr[i]


print("--- %s seconds ---" % (time.time() - start_time))


my_file = open("sort_selection{}.txt".format(amount), "w")
for i in range(0,amount):
    my_file.write(arr[i]+" ")
my_file.close()