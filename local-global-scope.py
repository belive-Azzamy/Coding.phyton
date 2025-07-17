x = 'global'
print(x, "diluar fungsi")

def foo():
    y = "local"
    print(x, "di dalam fungsi")
    print(y, "di dalam fungsi")

# print(y, "diluar fungsi") # error y is not defined

foo()

score = 0
print("score awal : ", score)

def tambah_score():
    global score
    score += 10
    print("score bertambah : ", score)

tambah_score()
tambah_score()
tambah_score()
print("score saat ini : ", score)

#overlapping variable
text = "global scope"
def myFunction():
   #print(teks)
   text = "local teks"
