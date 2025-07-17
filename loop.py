#Rewind
n = 1

while n < 6:
    print("I Like Python")
    n += 1

#For - Loop
names = ["Salamah", "Azzam", "Hafizh"]

for name in names:
    print("Hello " + name)

for i in range(2,11,2):
    print(i)

#Loop - Break
for i in range(11):
    print(i)
    if i == 5:
        break

#Loop - Continue
number = 0
while number < 10:
    number += 1
    if number == 5:
        continue
    print(number)

#Loop - Else
number = 0
while number < 10:
    number += 1
    if number == 5:
        continue
    print(number)
else:
    print("Loop's Finished")

for i in range(11):
    print(i)
    if i == 5:
        break
else:
    print("Loop's Finished")

#Loop - Pass
number = 0
while number < 10:
    number += 1
    if number == 5:
        continue
    print(number)
else:
    print("Loop's Finished")

for i in range(11):
    print(i)
    if i == 5:
        break
else:
    print("Loop's Finished")

#while True:
#   pass

#Nested Loop
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit in fruits:
    for color in colors:
        print(f"{fruit} with color {color}")
