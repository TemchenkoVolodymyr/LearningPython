# while , if continue
p = [0] * 10
i = 0
n = 1

while p.count(1) < 5 :
    print('s')
    n = int(input("Write a even number"))
    i += 1
    if p[n] == 1:
        print('t')
        continue

    p[n] = 1

print(*p)

# while , continue
n = 1
s = 1
while n != 0 :
    n = int(input())
    if  not n >= 1:
        continue
    s *= n
print(s)

# while , break
cities = list(map(str, input().split()))
i = 0
w_bool = 'ДА'
while i < len(cities):

    if len(cities[i]) < 5:
        w_bool = "НЕТ"
        break
    i += 1
print(w_bool)

# while , break
s = list(map(str,input().split()))

i = 0
w = 'НЕТ'
while i < len(s) :

    if s[i][-1] == s[i][0].lower():
        w = "ДА"
        break
    i += 1
print(w)

# while  else
n = int(input())
i = 1
m_lst = []

while i <= n and n <= 100:
    if i % 3 == 0 and i % 5 == 0:
        m_lst.append(i)
    i += 1


else:
    if n >= 100:
        print(f"слишком большое значение {n}")
    else:
        print(*m_lst)

# while else
n = int(input())

i = 1
while i**2 <= n :
    i += 1
else :
    print(i)

# while
x = int(input())
km = 10
d = 1

while km <= x :
    km += km * 0.10
    d += 1
print(d)

# while , remove() , lst[:] , contains()
lst_in = ['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
t = lst_in[:]
i = 1

while i <= len(lst_in)  :

    if lst_in[i - 1].__contains__(" ") :
        t.remove(lst_in[i - 1])
    i += 1
print(t)

