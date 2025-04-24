print("simple calculator")
print(20*"=")

number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))

result_add = number1 + number2 
print(f"{number1} + {number2} = {result_add}")

result_bagi = number1 // number2 
print(f"{number1} // {number2} = {result_bagi}")

result_kurang = number1 - number2 
print(f"{number1} - {number2} = {result_kurang}")

result_kali = number1 * number2 
print(f"{number1} * {number2} = {result_kali}")