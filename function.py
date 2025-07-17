print('Hello')

#function
def myFunction():
    print("It's my function")

myFunction()
myFunction()

#parameter
def sayHello(name, age):
    print(f"Hello {name}, are you {age} years old?")

sayHello("Hafizh", 12)
sayHello("Azzam", 15)
sayHello("Sal", 20)

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

y = tambah(10,20) * 5
print(y)

x = tambah(30, 21)
print(x)

number1 = 11
number2 = 12
add = tambah(number1, number2)
print(f"{number1} + {number2}")