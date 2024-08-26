## Если в конце print() прописать print("sdsa" , end=' ') - то не будет перехода на новую строчку после каждого элемента
## Если после итерации в цикле for написать просто print() без аргумента то будет перевод курсора на нижнюю строчку


## Пример того если список содержит вложенные списки и обычные элементы
# n = [1,2,3,[4,5,6],[10,12,22]]
#
# for x in n :
#
#     if type(x) == type([1,2,3]) :
#
#         for j in x :
#             print(j)
#     else :
#         print(x)

## for + for вложенный  . print("ds",end=" ")
# n = int(input())
# for x in range(1,n + 1) :
#     for j in range(1,n) :
#         print(1,end =" ")
#     print(5)

## for , enumerate
import sys
## считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# for i, x in enumerate(lst_in):
#     b = " ".join(x.split())
#     lst_in[i] = b
#
# for i, j in enumerate(lst_in):
#     b = j.replace(" ", "-")
#     lst_in[i] = b
#     print(lst_in[i])

## поиск простого числа в диапазоне заданого
# n = int(input())
#
# for x in range(2,n ) :
#     if x > 1 :
#         for j in range(2,x) :
#             if (x % j) == 0 :
#                 break
#         else :
#              print(x,end=" ")


## вложенные for , if , enumerate()
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# result = True
# for i, x in enumerate(lst_in):
#
#     for s_i, s_x in enumerate(x):
#         if s_x == 1:
#             if s_i + 1 in range(0, len(x) - 1):
#                 if lst_in[i][s_i + 1] == 1:
#                     result = False
#             if s_i - 1 in range(0, len(x) - 1):
#                 if lst_in[i][s_i - 1] == 1:
#                     result = False
#             if i + 1 in range(0, len(x) - 1):
#                 if lst_in[i + 1][s_i] == 1:
#                     result = False
#             if i - 1 in range(0, len(x) - 1):
#                 if lst_in[i - 1][s_i] == 1:
#                     result = False
#             if i + 1 in range(0, len(x) - 1) and s_i + 1 in range(0, len(x)):
#                 if lst_in[i + 1][s_i + 1] == 1:
#                     result = False
#             if i + 1 in range(0, len(x) - 1) and s_i + 1 in range(0, len(x)):
#                 if lst_in[i - 1][s_i + 1] == 1:
#                     result = False
#             if i - 1 in range(0, len(x) - 1) and s_i - 1 in range(0, len(x)):
#                 if lst_in[i - 1][s_i - 1] == 1:
#                     result = False
# print("ДА" if result else "НЕТ")

x = ['s','s','t']
print(len(x) - 1)


