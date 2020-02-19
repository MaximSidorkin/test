'''
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

numbers = (input('введите число - '))

sum_1 = numbers
sum_2 = numbers + numbers
sum_3 = numbers + numbers + numbers

all_is = int(sum_1) + int(sum_2) + int(sum_3)
print(all_is)
