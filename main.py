# дан отсортированный список
# нужно найти пару элементов сумма которых равна find_sum, нельзя в пару записать один и тоже элемент
import random

print(some_list := [x for x in range(1, 100, random.randint(1, 5))])  # генерирую список

find_sum = random.randint(1, 100)  # сумма для поиска

# сам алгоритм
left, right = 0, len(some_list) - 1
for i in some_list:
    while left != right:
        if some_list[left] + some_list[right] == find_sum:
            print(f'искомая сумма: {find_sum}, пара [{some_list[left]}, {some_list[right]}]')
            break
        elif some_list[left] + some_list[right] > find_sum:
            right -= 1
        elif some_list[left] + some_list[right] < find_sum:
            left += 1
    else:
        print(f'искомая сумма: {find_sum}, пара не нашлась')
    break
