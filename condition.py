today = "cerah"

if today == "cerah":
    print("Hari ini cerah kamu bisa main")
    print("Ga usah bawa payung")


battery_level = "full"

if battery_level == "low":
    print("your battery is low..")
    print("please, charge..")
else:
    print("your battery is full")

grade = input("Enter your grade (A/B/C): ")
grade = grade.upper()

if grade == "A":
    print("Congratulation..")
elif grade == "B":
    print("Good Job!")
elif grade == "C":
    print("Good luck next time..")
else:
    print("Wrong input")

score = 70

if score >= 70 and score <= 80:
    print("grade B")
elif score > 80 and score <= 85:
    print("grade B+")
elif score > 85 and score <= 90:
    print("grade A")
elif score > 90 and  score <= 100:
    print("grade A+")
else:
    print("grade C")

Hari = "Sabtu"

if Hari == "Sabtu" or Hari  == "Minggu":
    print("Hari libur")
else:
    print("Hari kerja")

usia = int(input("Masukkan usia kamu: "))
sim = input("Apakah kamu punya sim? Y/N : ")
sim = sim.upper()

if usia >= 17 and sim == 'Y':
    print("Anda diizinkan mengendarai kendaraan")
else:
    print("Anda tidak diizinkan mengendarai kendaraan")