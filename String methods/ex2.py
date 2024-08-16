#Methods

s = "hello"
print(id(s))
res = s.upper()
print(id(res))


# upper () , lower()
msg = "HELLO"
print(msg[0].upper() + msg[1 :].lower())

# count()

text = "between - me - and - you"
print(text.count("-"))

# find() , return index of letter

print(text.find("be"))

#replace()
text1 = "Hello---my--name---is---Python-"
firstReplace = text1.replace("---","--")
secondReplace = firstReplace.replace("--","-")
print(secondReplace)

# rjust() / ljust()
number = '1'
number2 = '23'
number3 = '132'
print(f"""{number.rjust(3,"0")}\n{number2.rjust(3,"0")}\n{number3}""")

# split()
countOfWords = "Hello Hello Hello"

print(len(countOfWords.split(" ")))

#replace()
cities = "London Kiev Moscow"
print(cities.replace(" ", ";" ))