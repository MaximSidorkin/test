'''
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
'''
z = []
revenue = int(input('значения выручки = '))
cost = int(input('издержек фирмы = '))

if revenue - cost > cost:
    print('прибыль больше издержек и равна ', revenue - cost)
    users = int(input('число сотрудников = '))
    salary = (revenue - cost) / users
    print('прибыль фирмы в расчете на одного сотрудника = ', salary)
else:
    print('прибыль меньше издержек')
