msg = "Тема занятия \"спецсимволы\""
# msg = 'Тема занятия "спецсимволы"'
print(msg)

# replace() + "\\"
text = "Hello World"
s = text.replace(" " , "\\")
print(s)

m = "My best friend is Python!"
firstReplace = m.replace(" ", "'" , 1)
secondReplace = firstReplace.replace(" ", "\"")
print(secondReplace)

#raw-str

rawStr = r"C:\WINDOWS\System32\drivers\etc\hosts"
print(rawStr)

# \" - double quotes
message = "language"
n = f"\"{message}\""
print(n)

### Format strings and F-strings

#format() --- the old method

name = "Volodymyr"
surname = "Temchenko"
age = "26"


print('Уважаемый {name} {surname}! Поздравляем Вас с {age} -летием!'.format(name=name,surname=surname,age=age))

## F-str + map() + split() + max() + min()
numbers = "11 18"
first,second = map(int,numbers.split())

print(f"{min(first,second)} {max(first,second)}")