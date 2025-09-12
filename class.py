#membuat class
class Animal:
    name = ""
    color = ""
#__init__
    def __init__(self):
        print("let us see this")

#class Method = prilaku g dapt dilakukan oleh objek, wajib memiliki 1 argumen yitu "self" = kata kunci
    def makeSound(self, sound):
        print(self.name, "is", sound)

#membuat objek
cat = Animal()

dog = Animal()

print(type(cat))
print(type(dog))

cat.name = "Kitty"
print(cat.name)
cat.color = "Orange"
print(cat.color)

dog.name = "Chippi"
print(dog.name)
dog.color = "Black"
print(dog.color)
cat.makeSound('meowing')
dog.makeSound('barking')

print("-"*57)

class Person:
    rambut = ""
    kulit  = ""

    def memakan(self, food):
        print("seseorang dengan warna rambut", self.rambut, "sedang memakan", food)
    def berjalan(self, gerakan):
        print("seseorang dengan warna kulit", self.kulit, "berjalan secara", gerakan)
person1 = Person()
person2  = Person()

person1.rambut = "hitam"
person2.rambut = "kuning"

person1.memakan("apple")
person2.memakan("mie")

person1.kulit = "putih"
person2.kulit = "sawo matang"

person1.berjalan("pelan")
person2.berjalan("cepat")

print("-"*20)

class Bread:
    material = ""
    textur   = ""
    
    def printed(self):
        print("bread made from", self.material, "is shaped into", self.textur)

bread = Bread()

bread.material = "wheat flour, eggs, and sugar"
bread.textur   = "circles"

bread.printed()

print("-"*20)

class Hewan:
    name = color = ""

    def __init__(self, animal_name, animal_color):
        self.name  = animal_name
        self.color = animal_color
    
    def info(self):
        print(f"Hewan dengan nama {self.name} memiliki warna {self.color}")

    def makeSound(self, sound):
        print(f"{self.name} with color {self.color} is making {sound}")

    def eat(self, food):
        print(f"{self.name} is eating {food}")

kucing = Hewan("Tom", "Dark blue")
kucing.info()
kucing.makeSound('meong')
kucing.eat('fish')

tikus = Hewan("Jerry", "Brown")
tikus.info()
tikus.makeSound("citcitt")
tikus.eat("cheese")