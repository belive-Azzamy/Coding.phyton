#membuat class
class Animal:
    name = ""
    color = ""

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


