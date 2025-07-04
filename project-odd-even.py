number = int(input("How many loop: "))
choise = input("Even or odd: ").lower()

if choise == "Even":
    for i in range(number):
        if i % 2 == 0:
            print(i)
elif choise == "odd":
    for i in range(number):
        if i % 2 == 1:
            print(i)
else:
    print("invalid input")
