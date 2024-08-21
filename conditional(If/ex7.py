# Ternary conditional operator
a = 2
b = 3
c = 4
s = "python"
u = "upper"
#"Обычный условный терарный оператор"

res = a if a > b else b
print(res)

test = s.upper() if u == "upper" else s
print(test)
#"Вложенный условный тернарный оператор"

d = (a if a > c else c ) if a > b else (b if b > c else c)
print(d)

# float() , if else  ternary condition
first = float(input())
second = float(input())
d = first if first > second else second
print(d)

# if else / number % 3 == 0
number = int(input())
msg = "кратно 3" if number % 3 == 0 else "не кратно 3"
print(msg)

# reverse() ,  "".join(w_reverse) - перевод обратно в строку  / if else
word = input().lower()
w_reverse = list(word)
w_reverse.reverse()
result = "".join(w_reverse)

print("палиндром" if result == word else "не палиндром")

#
number = input()
print(False if int(number) == 0 else True)

#
time = int(input())
print(0 if time == 59 else time + 1)

#
numbers = list(map(int,input().split()))
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
print(f"{'#' + m[numbers[1 - 1] - 1] if m[numbers[1 - 1] - 1] in ['до','фа'] else m[numbers[1 - 1] - 1] } {'#' + m[numbers[1] - 1] if m[numbers[1] -1 ] in ['до','фа'] else m[numbers[1] - 1]} {'#' + m[numbers[2] - 1] if m[numbers[2] -1 ] in ['до','фа'] else m[numbers[2] - 1]}")

