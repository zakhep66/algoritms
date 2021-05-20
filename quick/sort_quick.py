import time
import random
start_time = time.time()

amount = 10
file = open("db"+str(amount)+".txt")
arr=(file.read()).split(' ')

def quicksort(array):
   if len(array) <= 1:
       return array
   else:
       q = random.choice(array)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in array:
           if int(n) < int(q):
               s_nums.append(n)
           elif int(n) > int(q):
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)

arr2 = quicksort(arr)


print("--- %s seconds ---" % (time.time() - start_time))
# print (arr2)

my_file = open("sort_quick{}.txt".format(amount), "w")
for i in range(0,amount):
    my_file.write(str(arr2[i])+" ")
my_file.close