
## range()
# print(*list(range(0,11)))

## range(-10,1)
# print(*list(range(-10,1)))

## range(-10,-1,2)
# print(*list(range(-10,-1,2)))

## range(1,20,3)
# print(*list(range(1,20,3)))

## for
# n = list(map(int,input().split()))
# res = 0
# for x in n :
#     if x % 2 != 0 :
#         res += x
# print(res)

## range , for
# c = list(map(str, input().split()))
# for w in range(len(c)):
#     c[w] = len(c[w])
#
# print(*c)

## for in
# n = int(input())
# m = list(range(1,n +1))
#
# for x in m :
#     if n % x == 0 :
#         print(x)

## for in , break , else

# n = int(input())
#
# w = ""
# for x in range(2, n): ## чистое число которае - не содержит внутри своего диапазона числа при деление на которое будет 0
#
#     if n % x == 0:
#         w = "НЕТ"
#         break
# else:
#     w = "ДА"
# print(w)

## index(), for in , else
# c = list(map(str, input().split()))
# p_w = ""
# word = "ДА"
# for x in c:
#     i = c.index(x)
#     if i == 0:
#         p_w = c[0][-1].lower()
#     elif i != 0:
#         if x[-1] in ['ь', 'ъ', 'ы']:
#             if p_w != x[0].lower():
#                 word = "НЕТ"
#             p_w = x[-2]
#         else:
#             if p_w != x[0].lower():
#                 word = "НЕТ"
#             p_w = x[-1]
# print(word)

## for in , range()
# n = int(input())
# res = 0
# for x in range(1,n) :
#     if x % 3 == 0 or x % 5 == 0 :
#         res += x
# print(res)


