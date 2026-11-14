with open("contoh.txt", "w") as f:
    f.write("Belajar file handling\n")

with open("contoh.txt", "r") as f:
    isi = f.read()

print(isi)
print("File otomatis tertutup:", f.closed)
