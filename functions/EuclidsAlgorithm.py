# def test(numbers):
#
#     while numbers[0] != numbers[1] :
#         if numbers[0] > numbers[1] :
#              numbers[0] -= numbers[1]
#         else :
#              numbers[1] -= numbers[0]
#     return numbers[0]
#
#
# # print(test([18,24]))
# # help(test)  -- показывает описание функции
#
#
# def test_test(func):
#     a = 15
#     b = 121050
#     res = func([a,b])
#
#     return res
#
#
# print(test_test(test))

## Быстрый алгоритм Евклида . Выполнение операции занимает меньше секунды.
def get_nod(a,b):
    if a < b :
        a,b = b,a
    while b != 0 :
          a,b = b , a % b
    return a

