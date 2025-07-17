numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers)
print(type(numbers))
print(len(numbers))
print(numbers[4])

animals = ['cat', 'dog', 'fish', 'bird', 'panda']
print(animals)
print(type(animals))
print(len(animals))
print(animals[3])

countries = ['Indonesia', 'Malaysia', 'Singapore', 'Thailand']
print(countries)
print(type(countries))
print(len(countries))
print(countries[1])
countries[1] = 'Australia'
print(countries)

countries.append('Japan')
print(countries)

countries.remove('Thailand')
print(countries)

countries.clear()
print(countries)