
# while , append()
numbers = input()
n,m = map(int,numbers.split())
i = n
lst = []
while i <= m :
    lst.append(i**2)
    i += 1
print(*lst)

# append,round(), while
price = float(input())
count = 2
prices = []
while count <= 10 :
    prices.append(round(price * count,2))
    count += 1
print(*prices)

# round(),while, for , in
number = int(input())
numbers = []
i = 1
while i <= number :
    numbers.append(i)
    i += 1
result = sum(1/ number for number in numbers)
print(round(result,3))

# while
number = int(input())
total = 0
while number != 0 :
    total += number
    print(1)
    number = int(input())

print(total)

#
msg = "dsad--dsad---dsad----"

while msg.count("--") or msg.count("---") or msg.count("----"):
    msg = msg.replace("--", "-")

print(msg)

# while
n = list(map(int,input()))
i = 1
total = 1
while i <= len(n) :
    total *= n[i - 1]
    i += 1
print(total)

# while , append
n = int(input())
i = 2
result = [1,1]
while i < n :
    result.append(result[- 1] + result[-2])
    i += 1
print(*result)

# while , if not
n = int(input())
m = 0
k = 1

while m < n:

    if not m + 3 > n:
        k *= 2
    m += 3
print(k)

# round , while
n = int(input())
i = 0
res = 1000
while i < n :
    res = res + (res * 0.05)
    i += 1
print(round(res,2))

# while , append() , list
i = 100
lst = []
while 100 <= i <= 999 :
    if i % 47 == 43 and i % 3 == 0 :
        lst.append(i)
    i += 1
print(*lst)


