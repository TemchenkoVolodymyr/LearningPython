## create list
# number1,number2,number3 = map(int,input().split())
# numbers = [number1,number2,number3]
# print(numbers)
#
#
# ### operator in
#
# cities = ["Moscow", "Kiev", "London"]
#
# print("Moscow" in cities)
#
# ## last element in the list
#
# print(cities[-1])
#
#
# ## sum() + len() + round()
# marks = list(map(int, input().split()))
# total = sum(marks) / len(marks)
#
# print(round(total , 1))

##  del , float() , len()

# a = input()
# b = input()
# c = input()
# d = input()
#
# book = [a,b,c,d]
# del book[2]
# book[1] = "Pushkin"
# price = book[len(book) -1]
# float_price = float(price) + float(price)
# book[len(book) -1] = float_price
# print(book)

##  max() , min() , sum() , list
# if you want to receive numbers ---- subs = list(map(int,input().split()))

# subs = list(map(int,input().split()))
# subs_max = max(subs)
# subs_min = min(subs)
# subs_total = sum(subs)
# print(subs_max , subs_min , subs_total)

##  sorted() , list(), *lst_sorted - delete all symbols [,]
# lst = list(map(int,input().split()))
# lst_sorted = sorted(lst,reverse=True)
#
# print(*lst_sorted)

##  operator + , list() , *new_list
# cities = ["Москва", "Тверь", "Вологда"]
# old_cities = list(input().split())
# new_list = cities + old_cities
# print(*new_list)

#####            list cut

# v = [1205, 1101, 1434, 1320, 923, 874]
#
# print(v[:3])

# v = [1205, 1101, 1434, 1320, 923, 874]
# print(v[-4 : ])
#
# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[: : 2])

# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[1 : : 2])

## reverse() + list()
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# m_rever = m[2 : 7]
# m_rever.reverse()
# print(m_rever)

##  m[::::]  [-1::-2]

# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
#
# print(m[-1 ::-2])    # Start from end , step -2 because we have -



