# create file : x
'''
 after creat the file in the folder, save it with "ctrl + s",
 if you wan to unsave just "ctrl + z"
'''

try:
    file = open('file-handling/biodata.txt', 'x')
except FileExistsError:
    print("File sudah ada!")

# read file : r
try:
    file = open('file-handling/biodata.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print("File Not Found!")

# wtite file : w

file = open('file-handling/note.txt', 'w')
file.write("The most popularprograming languege\n")
file.write("1. Python\n")
file.write("2. Javascript")

text = '''
3. Golang
4. Ruby
'''

file.write(text)
file.close()

# append file
file = open('file-handling/note.txt', 'a')
file.write("5. Java")
file.write("\n6. SQL")
file.close()

file = open('file-handling/todolist.txt', 'a')
file.write("To Do List")
text = '''
1. Study
2. Shopping
'''
file.write(text)
file.close()