try:
    file = open('my-bio/my-data.txt', 'x')
except FileExistsError:
    print("File ini sudah ada")

file = open('my-bio/my-data.txt', 'w')
file.write("About Me\n")
file.write("Hello, my name is Azzam.\n")
file.write("I am 15 years old, and my hoby is reading novels.\n")
file.write("what about my ambition? My ambition is to become a professional financial consultant bos\n")
file.write("InsyaAllah.\n")

text = '''
I hope I can achieve my dream
'''
file.write(text)
file.close()

file = open('my-bio/my-data.txt', 'a')
file.write("Amen\n")
file.close()

try:
    file = open('my-bio/my-data.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print("File Not Found!")