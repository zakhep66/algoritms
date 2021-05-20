import random

p = False
while (p == False) :
    print("Сколько чисел вы хотите сгенирировать?")
    amount = input()
    if (amount.isdigit() == False):
        print('Ошибка ввода')
    p = amount.isdigit()

a = []
for i in range(0,int(amount)):
    a.append(random.randint(1,1000000))

my_file = open("{}.txt".format(amount), "w")

for i in range(0,int(amount)):
    
    if (i != ((int(amount)-1))):
        my_file.write(str(a[i])+" ")
    else:
        my_file.write(str(a[i]))


my_file.close()