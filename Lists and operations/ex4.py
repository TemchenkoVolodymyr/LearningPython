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



## list() , if else , append() , len()
# lst = list(input().split())
# if lst[0] != lst[len(lst) - 1] :
#     lst.append(True)
#
# else :
#     lst.append(False)
# print(*lst)

## insert()

# cities = ["Moscow", "London", "Kiev"]
# cities.insert(1,"New York")
# print(*cities)

## list()  , remove() , while , in , join() , index()

# tel = list(input())
# tel.remove("+")
# find_index = tel.index("7")
# tel[find_index] = "8"
# while "-" in tel :
#     tel.remove("-")
# print("".join(tel))

##

# fio = input()
# first_name,middle_name,last_name = fio.split()
# initials = f"{last_name} {first_name[0]}.{middle_name[0]}."
# print(initials)

## map() , while , remove() , append() , min()
# numbers = list(map(int,input().split()))
# a = 1
# found_num = []
# while a <= 3 :
#     min_number = min(numbers)
#     found_num.append(min_number)
#     numbers.remove(min_number)
#     a += 1
#
# print(*found_num)


## if else , append(),pop()

# lst = list(map(int, input().split()))
# del_item = lst.pop()
# if del_item % 2 == 0:
#     lst.append(False)
# else:
#     lst.append(True)
#
# print(*lst)

## count()

# marks = list(map(int,input().split()))
# a = marks.count(2)
# print(a)

## sort() , pop()
# reavers = list(input().split())
# reavers.sort()
# reavers.pop(0)
# print(*reavers)

#####  Sublists

# lst = [5.4, 6.7, 10.4]
# digs = list(map(int,input().split()))
# lst.append(digs)
# print(lst)

## append() , list() , []
# first = list(input().split())
# second = list(input().split())
# third = list(input().split())
# stack = []
# stack.append(first)
# stack.append(second)
# stack.append(third)
# print(stack)

## append() , list,map()
# lists = []
# first = list(map(int,input().split()))
# second = list(map(int,input().split()))
# third = list(map(int,input().split()))
# lists.append(first)
# lists.append(second)
# lists.append(third)
#
# print(lists[0][3],lists[1][3],lists[2][3])

## in
# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#      ["Я", "Python", "выучил", "с", "каналом"],
#      ["Балакирев", "что", "раздавал?"]]
#
# # здесь продолжайте программу
# word = input()  // дядя
#
# print(word in t[0] + t[1] + t[2])