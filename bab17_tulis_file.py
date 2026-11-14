with open("data.txt", "w") as f:
    f.write("Baris pertama\n")
    f.write("Baris kedua\n")

with open("data.txt", "a") as f:
    f.write("Baris ketiga\n")

print("File data.txt berhasil ditulis")
