#Tuple
numbers = (0,1,2,3,4,5)
print(numbers)
print(type(numbers))

print(numbers[3])
# numbers[3] = 13 # error

#Tuple manipulation
location = tuple(('103.99', '-23.88'))
print(location)
print(type(location))

num_list = list(numbers)
print(num_list)
print(type(num_list))

num_list[5] = 10
print(num_list)

num_tuple = tuple(num_list)
print(num_tuple)
print(type(num_tuple))
