student = {
    "Name" : "Ahmad",
    "Grade" : 10,
    "Addres" : "Jakarta",
    "Beasiswa" : True,
    "Prestasi" : ["Juara 1 Math", "Juara 2 Science"],
}

print(student)
print(type(student))

key_student = student.keys()
print(key_student)

print(student["Beasiswa"])
print(student["Prestasi"])

for key in student:
    print(key, ":", student[key])

student["Addres"] = "Tangerang"
print(student)

student['Email'] = 'Ahmad@student.gmail'
print(student)

student.pop("Beasiswa")
print(student)

student.popitem()
print(student)

student.clear()
print(student)

student2 = dict(fullname="Azzamy muttaqin", addres="Penajam", skills=["Volley", "Video Editor"])
print(student2)
print(type(student2))