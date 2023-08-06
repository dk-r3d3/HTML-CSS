# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы используется множество
# раз и вы не хотите ничего сломать):

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

"""
Список кортежей рандомный из 2 цифр с двумя полуосями
ОДИНАКОВЫХ ОСЕЙ БЫТЬ НЕ МОЖЕТ
САМАЯ БОЛЬШАЯ ПЛОЩАДЬ САМАЯ ДАЛЬНЯЯ 
найти площадь piab орбит
далее функция принимает значения кортежей и возвращает самый большой
S = piab
"""
# import math
# from random import randint

# lst = [(randint(1, 10), randint(1, 10)) for i in range(5)]
# planets = list(filter(lambda x: x[0] != x[1], lst))
# print(lst)
# print(planets)
# print(max(planets, key=lambda x: x[0] * x[1]))

# def find_farthest_orbit(list_of_orbits):
#     list_res = []
#     for i,j in list_of_orbits:
#         # list_res = list(lambda x: (math.pi * i * j), i != j)
#         if i != j:
#             S = math.pi * i * j
#             list_res.append(S)
#     max_s = max(list_res)

#     res = list_of_orbits[list_res.index(max_s)]
#     print(list_res)
#     return res

# print(lst)
# print(find_farthest_orbit(lst))

# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.

# object = 'asd asd asd asd'
# def same_by(characteristic, objects):
#     lst = list(map(str,objects.split()))
#     if map(lambda x: len(x) == characteristic, lst):
#         return True
#     return False
#     # print(max(lst, key = lambda x: len(x)
#     # list(filter(lambda x: x[0] != x[1], lst))

#     # return lst
# print(same_by(3, object))

# def same_by(func, array):
#     if len(array) == 0:
#         return True
#     buf = list(map(func, array))
#     if len(list(filter(lambda x: x == buf[0], buf))) == len(buf):
#         return True
#     return False

# print((lambda a, b: a if a > b else b)(25, 12))
# print((lambda a, b: a * b)(12, 1))

# obj = 'asd asd asd asd'



# def res(obj):
#     control = list(map(len, obj.split()))
#     return 



# print(lst_obj)
# print(control)