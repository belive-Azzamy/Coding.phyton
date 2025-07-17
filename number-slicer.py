# create a variable called 'numbers'
# creat a list of numbers 1 - 250 using list(range())
numbers = range(1,251)
print(list(numbers))

# print a number from index 15
numbers = list(numbers)
print(numbers)
print(numbers[15])

# print an eight number from the back
# clue : negative indexing
print(numbers[-8])

# print a group of numbers, start from 55(number) until 67
print(numbers[54:67])


# print a group of even numbers, starts from 70(number) until 240
# clue : use step parameter
print(numbers[69:240:2])