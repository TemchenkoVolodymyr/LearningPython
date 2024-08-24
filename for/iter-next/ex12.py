# iter() - создает итерацию элементов списка, строки которую получил
# next() - читает по очереди элементы списка или строки
# Когда доходит до конца , выдает ошибку stopIteration
c = list(map(str,input().split()))
c_it = iter(c)

print(next(c_it))
print(next(c_it))

# iter() , next() , for in

st = input()
st_it = iter(st)
res = ""
for x in st_it :
    if x == " " :
        break
    else :
        res += x
print(res)

# iter,next,for in
n = input()
n_it = iter(n)
res = ""
for x in n :
    res += " " + x


print(res)