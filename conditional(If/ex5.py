# if else
nums = list(map(float, input().split()))
if nums[0] > nums[1]:
    print(nums[0])

else:
    print(nums[1])

# lower() , if else , [::-1] = reverse string
word = input().lower()

if word == word[::-1]:
    print("ДА")
else :
        print("НЕТ")

# if else
numbers = input()
m,n = map(int,numbers.split())
if m % n == 0 :
    print( int(m / n) )
else :
    print(f"{m} на {n} нацело не делится")

# 2**2 - возвездение в степень
numbers = list(map(int, input().split()))
if numbers[0] ** 2 + numbers[1] ** 2 == numbers[2] ** 2:
        print("ДА")
else:
        print("НЕТ")

# if else , len() , str()
number = input()
if number[len(number) - 1] == str(7) :
    print("ДА")
else : print("НЕТ")

# count() , if else
msg = input()
if msg.count('t') and msg.count('h') and msg.count('o') :
    print("ДА")
else : print("НЕТ")

# remove , if else , count

cities = list(input().split())
if cities.count("Москва") :
    cities.remove("Москва")
print(*cities)

#
a,b,c,d=map(int,input().split())
if b > a:
     a, b = b, a
if d > c:
     c, d = d, c
if (a - c >= 2 and b - d >= 2):
     print('ДА')
else:
     print('НЕТ')


# map , list , if else , sum()
number = input()
f_half = list(map(int, number[: 3]))
s_half = list(map(int, number[3:]))
if sum(f_half) == sum(s_half):
         print("ДА")
else:
         print("НЕТ")


## if else ,
times = input()
new_time = list(times)

if len(new_time) >= 2:
    if 0 <= int(new_time[1]) <= 2 or 7 <= int(new_time[1]) <= 9:
        print("green")
    else:
        print("red")
else:
    print("red")