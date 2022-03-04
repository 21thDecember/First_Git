import random
letters = ["a","b","c","d","e","f","g"]
numbers = [1,2,3,4,5,6,7,8]
symbols = ["!", "@", "#", "$", "%", "^"]
a = int(input("How many letters? "))
b = int(input("How many numbers? "))
c = int(input("How many symbols? "))
password = ""
for i in range(a):
    temp = random.choice(letters)
    password = password + temp
for i in range(b):
    temp = random.choice(numbers)
    password = password + str(temp)
for i in range(c):
    temp = random.choice(symbols)
    password = password + temp
print(password)