#args
def addition(a,b):
    add = a + b
    print(add)

addition(1,2)
# addition(1) #error

#arbitrary argumen, *args
def total(*numbers):
    result = 0
    for num in numbers:
        result += num
    print("total = ", result)

total(1,2,3,4,5,)
total(10,20,30)
total(88,77)

#keywar arguments
def fullname(fname, lname):
    print("Firs name:", fname)
    print("Last name:", lname)

fullname(fname="Jaka", lname="Argantara")
fullname("Argantara", "Jaka")

#arbitrary keyword arguments
def namalengkap(**name):
    for key, value in name.items():
        print(key,value)
    
namalengkap(
    nama_depan = "Azzamy",
    nama_belakang = "Muttaqin"
)

#devault value
def sayHello(name,message="Hello"):
    print(message, name, "!")

sayHello("Salma")
sayHello("Azzam", "Hai")

sayHello(
    message="Assalamu'alaikum",
    name="Azzam"
)
