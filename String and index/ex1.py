# 1
msg1 = "Hello"
msg2 = "Python"

print(msg1[ : len(msg1)  : 2] + " " + msg2[1: len(msg2) : 2])

# 2
msg = "abrakadabra"
reverseMsg = msg[: 5]
print(reverseMsg[: : -1])

# 3
first = "Hoho"
second = "Motorcycle"
print(second[: len(first)])

# 4

word1 = "Hello"
word2 = "Hell"
cutWord = word1[: len(word2)]
print(cutWord[1 :  : 2] == word2[1 :  : 2])