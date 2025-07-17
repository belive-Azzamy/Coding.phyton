student = "Alhazen"
try:
    print(stdent)
except NameError:
    print("Variable tidak ditemukan")
except:
    print("Error!!")
else:
    print("run succesfully")
finally:
    print("scrip has run")

for i in range(10):
    print(i)

print("I like python App")
print(30*"=")

loop = int(input("Enter a number: "))

if loop <= 1:
    raise Exception("Number must be > 1")
         #/ValueError
else:
    for i in range(loop):
        print("I like python")
