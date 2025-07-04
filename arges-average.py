def rata_rata(*numbers):
    result = 0
    for num in numbers:
        result += num
    n = len(numbers)
    print("rata_rata = ",result/n)

rata_rata(1,2,3,4,5)
rata_rata(10,20,30)
rata_rata(55,55)
