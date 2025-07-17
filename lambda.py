# lambda vynt

def greeting(name):
    print(f"Hallo {name}")

greeting("Miss Salamah")

greeting2 = lambda name : print(f"Hallo {name}")

greeting2("Azzam")

def is_even(number):
    if number % 2 == 0:
        print("Yes number is even")
    else:
        print("No, the number is odd")

is_even(4)
is_even(5)

is_even2 = lambda number : print("Yes") if number % 2 == 0 else print("No")

is_even2(10)
is_even2(13)