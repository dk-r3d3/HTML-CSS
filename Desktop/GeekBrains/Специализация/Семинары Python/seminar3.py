# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

# from random import randint

# n = int(input("Введите количество чисел N: "))
# k = int(input("Введите сдвиг K: "))

# list_1 = [randint(1, 10) for i in range(n)]
# print(list_1)


# list_2 = []

# for i in range(n - k, n):
#     list_2.append(list_1[i])

# print(list_2)
# list_3 = list_1.pop(-1, -k)
# print(list_3)

# Напишите программу для печати всех уникальных значений в словаре.

# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# list_2 = []

# for i in list_1:
#     for key, value in i.items():
#         list_2.append(value)

# print(list_2)
# print(set(list_2))

# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

# x = [1, 2, 0, -1, 4, 5]

# for i in range(1, len(x)):
#     print(x[i])