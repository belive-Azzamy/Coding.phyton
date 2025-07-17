def countdown(number):
    print(number)
    if number == 0:
        return
    else:
        countdown(number-1)

countdown(100)

space = "        "
print(space)

def factorial(number):
    print(number)
    if number == 1:
        return 1
    else:
        result = number * factorial(number-1)
        return result
    
lima_faktorial = factorial(5)
print(lima_faktorial)

space = "        "
print(space)

a = factorial(10)

space = "        "
print(space)

print(a)