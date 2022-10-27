#первая часть: накопленные средства за год вклада в каждом из банков
money = int(input('Введите сумму вклада'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_list = list(per_cent.values())

a = int((per_cent_list[0] * money) / 100)
b = int((per_cent_list[1] * money) / 100)
c = int((per_cent_list[2] * money) / 100)
d = int((per_cent_list[3] * money) / 100)

deposit = [a, b, c, d]
print(deposit)

#вторая часть: найти максимальное значение среди элементов в списке
i = max(deposit)
print('Максимальная сумма, которую вы можете заработать', i)
