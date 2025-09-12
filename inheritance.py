#parent class
#sebagai data utama tetap
class Person:
    name = ""
    age = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print(f"This person's name {self.name} {self.age} years old")

person1 = Person("Hafizh", 13)
person1.getInfo()

person2 = Person("Azzam", 15)
person2.getInfo()

#Child class
#sebagai data yg mau diganti" sesuai dengan variable class child masing"
class Student(Person):
    def __init__(self, name, age, nis):
        super().__init__(name, age)
        self.nis = nis
    
    def study(self, subject):
        print(f"{self.name} with NIS {self.nis} study {subject}")
    #Overriding
    def getInfo(self):
        print(f"This student's name {self.name} with NIS {self.nis}, {self.age} years old")

student1 = Student("Salama", 16, "20250101")
student1.getInfo()
student1.study("Math")

print("-"*20)
#project
class Teacher(Person):
    def __init__(self, name, age, nip):
        super().__init__(name, age)
        self.nip = nip
    def teaching(self, subject):
        print(f"{self.name} is teaching {subject}")

    def getInfo(self):
        print(f"This teacher's name {self.name} with NIP {self.nip}, {self.age} years old")

teacher1 = Teacher("Pak Budi", 30, "20205432")
teacher1.getInfo()
teacher1.teaching("Math")