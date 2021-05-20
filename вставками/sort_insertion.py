import time
start_time = time.time()

amount = int(input('количество элементов: '))
file = open('../генератор/' + (str(amount))+".txt", "r")
arr=(file.read()).split(' ')


for i in range(1, len(arr)):
    item_to_insert = int(arr[i])
    j = i - 1

    while j >= 0 and int(arr[j]) > item_to_insert:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = item_to_insert

print("--- %s seconds ---" % (time.time() - start_time))


my_file = open("sort_insertion{}.txt".format(amount), "w")
for i in range(0,amount):
    my_file.write(str(arr[i])+" ")
my_file.close