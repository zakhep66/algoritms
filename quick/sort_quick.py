import time
import random
start_time = time.time()

amount = int(input('количесmво элементов: '))
file = open('../генератор/' + str(amount) + ".txt", "r")
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

my_file = open("sort_quick{}.txt".format(amount), "w")
for i in range(0,amount):
    my_file.write(str(arr2[i])+" ")
my_file.close







import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
           if len(nums) <= 1:
               return nums
           else:
               q = random.choice(nums)
               s_nums = []
               m_nums = []
               e_nums = []
               for n in nums:
                   if int(n) < int(q):
                       s_nums.append(n)
                   elif int(n) > int(q):
                       m_nums.append(n)
                   else:
                       e_nums.append(n)
               return Solution().sortArray(s_nums) + e_nums + Solution().sortArray(m_nums)