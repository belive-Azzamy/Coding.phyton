numbers = {1,2,3,4,5,2,6,3}
print(numbers)
print(type(numbers))

fruits = {'Apple', 'Banana', 'Durian', 'Apple'}
print(fruits)
print(type(fruits))

# print(fruits[1]) "[2],[3] # error
for fruit in fruits:
    print(fruit)

# add
fruits.add('Watermelon')
print(fruits)

# discard
fruits.discard('Banana')

# remove
fruits.remove('Durian')

# fruits.remove('Mango') # error
#print(fruits)

#pop --> remove random item
fruits.pop()
print(fruits)

animals = {'Cat', 'Dog', 'Wolf', 'Bird', 'Fox'}
amphibians = {'salamander', 'Frog'}
            # set(('Salamander', 'Frog'))

print(animals)
print(amphibians)

animals.update(amphibians)
print(animals)

mamalia = ['Dolphin', 'Whale']
animals.update(mamalia)
print(animals)