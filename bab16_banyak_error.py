data = ["abc", "12", None]

for item in data:
    try:
        angka = int(item)
        print("Angka:", angka)
    except ValueError:
        print("Bukan angka:", item)
    except TypeError:
        print("Tipe data salah:", item)
