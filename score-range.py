grade = int(input("Masukkan nilai kamu: "))

if grade >= 85 and grade <= 100:
    print("Nilai kamu A")
elif grade > 70 and grade <= 85:
    print("Nilai kamu B")
elif grade > 50 and grade <= 70:
    print("Nilai kamu C")
elif grade < 50:
    print("Nilai kamu D")
else:
    print("Terjadi kesalahan dalam memberikan informasi")