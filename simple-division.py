try:
    number = int(input("Enter youre first number: "))
    number2 = int(input("Now enter youre second number: "))

    div = number / number2
    print(f"{number} / {number2} = {div}")
except ZeroDivisionError:
    print("Number can't zero")
except ValueError:
    print("Can't input other than number")
except:
    print("Error!!")
