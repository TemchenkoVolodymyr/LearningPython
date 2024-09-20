## function declaretion
# def print_message():
#     print("It's my first function")
# print_message()
#
# ##
# def print_message():
#     name,surname = input().split()
#     print(f"Уважаемый, {name} {surname}! Вы верно выполнили это задание!")
# print_message()

##
# def set_total(weight):
#     print(f"Предмет имеет вес: {weight} кг.")
#
# number = input()
# set_total(number)

## min(),max(), list, function , sum()
# def set_sum(items):
#     min_number = min(items)
#     max_number = max(items)
#     total = sum(items)
#     print(f"Min = {min_number}, max = {max_number}, sum = {total}")
# numbers = list(map(int,input().split()))
# set_sum(numbers)

##
# def findPerimeter(width, height):
#     per = (width + height) * 2
#
#     print(f"Периметр прямоугольника, равен {per}")
#
#
# width, height = input().split()
#
# findPerimeter(int(width), int(height))

##
# def validEmail(email):
#     if email.count("@") and email.count("."):
#         for word in email:
#             if "A" <= word <= "Z" or "a" <= word <= "z" or word == "_" or "0" <= word <= "9":
#
#                 return True
#             else:
#                 return False
#     else:
#         return False
#
#
# emailToValid = input()
#
# print("ДА" if validEmail(emailToValid) else "НЕТ")

## function return
# def  get_sq(even):
#     return even **2
#
# number = float(input())
# print(get_sq(number))

##
# def is_triangle(f,s,t):
#     if f < s + t and s < f+t and t < f + s :
#         return True
#     return False

##
# def is_large(message):
#     return False if len(message) < 3 else True

##
# def isEven(number):
#     return True if number % 2 == 0 else False
#
#
# x = int(input())
# while x != 1:
#     if isEven(x):
#         print(x)
#     x = int(input())
##
# def test(number):
#     return True if number % 2 != 0 else False
# lst_d = list(map(int, input().split()))
#
# lst = []
# for char in lst_d :
#     if test(char) :
#         lst.append(char)
# print(*lst)
#
# ##
# tp = input().strip()
#
# #здесь продолжайте программу
#
# if tp == "RECT" :
#     def get_sq(height,weight):
#         return  height * weight
# if tp != "RECT" :
#     def get_sq(height):
#         return height * height

##
# put your python code here

# def test(str):
#     return False if len(str) < 6 else True
# cities = list(map(str,input().split()))
# lst = []
#
# for char in cities :
#     if test(char) :
#         lst.append(char)
# print(*lst)

##
# def get_len(s):
#     return s, len(s)
#
#
# d = {s: len(s) for s in input().split()}
# a = sorted(d, key=lambda x: d[x])
# print(*a)


