# abs() , create list by for in
lst = list(map(float,input().split()))

lst_abs = [abs(x) for x in lst ]
print(lst_abs)

##
n = input()

a = [int(x) for x in n]
print(a)

## for in , enumerate , []
N = int(input())
lst = []
for i in range(N):
    lst.append([0] * N)

for j, x in enumerate(lst):
    if j != len(x) - 1:
        lst[0][0] = 1
        lst[j + 1][j + 1] = 1

    else:
        if j == len(x) - 1:
            lst[j][j] = 1

    print(*x)

# [List comprehension]
c = [x for x in input().split() if len(x) > 5]
print(*c)

# [List comprehension]
n = int(input())

lst = [x for x in range(1,n + 1) if n % x == 0]
print(*lst)

#
N = int(input())

lst = [[x] * N  for x in range(0,N)]

for y in lst :
    print(*y)

#
n = list(input().split())
lst = [x for i,x in enumerate(n) if i % 2 == 0 ]
print(*lst)

#
first = list(input().split())
second = list(input().split())

lst = [int(x) + int(second[i]) for i,x in enumerate(first)]
print(*lst)

#
msg = input().split()

lst = [[ms , int(msg[i + 1])] for i,ms in enumerate(msg) if i != len(msg) - 1  if not ms.isdigit()]

print(lst)

