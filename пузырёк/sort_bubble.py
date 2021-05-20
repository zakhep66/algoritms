import time
start_time = time.time()

amount = int(input('количесmво элементов: '))
file = open('../генератор/' + str(amount) + ".txt", "r")
arr=(file.read()).split(' ')


for i in range(amount-1):
    for j in range(amount-i-1):
        if (int(arr[j]) > int(arr[j+1])):
            arr[j], arr[j+1] = arr[j+1], arr[j]


print("--- %s seconds ---" % (time.time() - start_time))


my_file = open("sort_bubble{}.txt".format(amount), "w")
for i in range(0,amount):
    my_file.write(arr[i]+" ")
my_file.close