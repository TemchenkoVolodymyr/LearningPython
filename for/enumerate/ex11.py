# enumerate() , for , if
w = input()
isWord = False

result = []
for i, x in enumerate(w):

    if i != len(w) - 1:

        if x == "р" and w[i + 1] == "а":
            result.append(i)
            isWord = True

if isWord:
    print(*result)
else:
    print(-1)

# for , elif
n = input()
t = "+7(xxx)xxx-xx-xx"
f = "ДА"

if len(n) - 1 != len(t) - 1:
    f = "НЕТ"

for i, x in enumerate(n):
    if not x in ["+", "-", "(", ")"]:
        if not x.isnumeric():
            f = "НЕТ"

    if not n[0] == "+":
        f = "НЕТ"
    elif not n[2] == "(":
        f = "НЕТ"
    elif not n[6] == ")":
        f = "НЕТ"
    elif not n[10] == "-":
        f = "НЕТ"
    elif not n[13] == "-":
        f = "НЕТ"
    elif not n[1] == "7":
        f = "НЕТ"

print(f)

# isdigit() - True / False .  Проверяет содержит ли строка число. Может быть число только  в таком виде "7". Если будет 7 , будет ошибка


# isdigit() , enumerate , for in , if else ,append(),replace()
m = input()
m = m.replace(" ", "")
m = m.replace("+", " + ")
m = m.replace("-", " - ")
m = m.replace('"', "")
m_lst = m.split(" ")

l = []
result = 0


for x in m_lst:
    if x in ["-", "+"]:
        l.append(x)

    else:
        if l and l[-1].isdigit():
            l[-1] += x
        else:
            l.append(x)

for i, x in enumerate(l):

    if x.isdigit():

        if i < len(l)  and i != 0:
            print(x)
            if l[i - 1] == "+":
                result += int(x)
            else:
                result -= int(x)
        else:
            if i == 0:

                if l[i + 1] == "+":

                    result += int(x)
                else:

                    result -= int(x)
print(result)

# for , enumerate()
lst = list(map(int,input().split()))

for i,x in enumerate(lst) :
    lst[i] = x * x
print(*lst)

# for , append
lst = list(map(str, input().split()))
new_lst = []
for i, x in enumerate(lst):
    new_lst.append(x)
    new_lst.append(x)
lst = new_lst
print(*lst)

# for in
n = list(map(float, input().split()))
n_min = n[0]
for x in n:
    if x < n_min:
        n_min = x

print(n_min)

# enumerate(), for in
n = list(map(float,input().split()))

for i,x in enumerate(n) :
    if x < 0 :
        n[i] = -1.0
print(*n)



