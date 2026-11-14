hitungan = 1
while hitungan <= 5:
    print("Hitungan:", hitungan)
    hitungan += 1

for n in range(1, 10):
    if n == 3:
        continue
    if n == 6:
        break
    print("Angka:", n)
