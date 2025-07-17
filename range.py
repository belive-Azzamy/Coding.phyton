numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

numbers2 = range(11) #stop (n-1)
print(list(numbers2))

numbers3 = range(101) #stop (n-1)
print(list(numbers3))

numbers4 = range(1,21) #start,stop (n-1)
print(list(numbers4))

numbers5 = range(4,31)  #start,stop (n-1)
print(list(numbers5))

numbers6 = range(4,31,2)    #start,stop (n-1), step
print(list(numbers6))

numbers7 = range(0,105,5)   #start,stop (n-1), step
print(list(numbers7))

numbers = list(numbers7)
print(numbers)

#indexing
print(numbers[5])
print(numbers[8])
print(numbers[-1])
print(numbers[-4])

#slicing
print(numbers[5:8]) #start:stop (n-1)
print(numbers[0:10]) #start:stop (n-1)
print(numbers[:10]) #start:stop (n-1)
print(numbers[-10:]) #start:stop (n-1)
print(numbers[1:11:2]) #start:stop (n-1): step
print(numbers[-10:-1:2]) #start:stop (n-1): step