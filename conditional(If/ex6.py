## Диапазон от 0 до 10  // Больше или равно  0 но меньше или равно 10
# x = 11
#
# if 0 <= x <= 10 :
#     print(x)
# else :
#     print(0)

## if , elif
# number = int(input())
# m = ["1. Введение в Python", "2. Строки и списки", "3. Условные операторы", "4. Циклы",
#          "5. Словари, кортежи и множества", "6. Выход"]
#
# if number == 1:
#     print(m[number - 1])
# elif number == 2:
#     print(m[number - 1])
# elif number == 3:
#     print(m[number - 1])
# elif number == 4:
#     print(m[number - 1])
# elif number == 5:
#     print(m[number - 1])
# elif number == 6:
#     print(m[number - 1])


##  if else
# numbers = list(map(int,input().split()))
#
# if numbers[0] < numbers[1] :
#     if numbers[0] < numbers[2] :
#         print(numbers[0])
#     else :
#         print(numbers[2])
# else :
#     if numbers[1] < numbers[2] :
#         print(numbers[1])
#     else :
#         print(numbers[2])

## if elif
# weight = float(input())
# if weight <= 60 :
#     print(1)
# elif 60 < weight <= 64 :
#     print(2)
# elif 64 < weight <= 69 :
#     print(3)
# elif weight > 69 :
#     print(4)

## if , []
# day = int(input())
# week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# if 0 <= day <= 7 :
#     print(week[day - 1])

## if elif
# day = int(input())
# if day == 2 :
#     print(28)
# elif day == 1 or day == 3 or day == 5 or day == 7 or day == 8 or day == 10 or day == 12 :
#     print(31)
# elif day == 4 or day == 6 or day == 9 or day == 11 :
#     print(30)
month = '7'
print(f"{int(month) + 1}.01")