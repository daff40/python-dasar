nilai = {"matematika": 85, "inggris": 90, "pemrograman": 95}

for mapel in nilai:
    print(mapel)

for mapel, angka in nilai.items():
    print(mapel, "=", angka)

print(list(nilai.keys()))
print(list(nilai.values()))
print("Rata-rata:", sum(nilai.values()) / len(nilai))
