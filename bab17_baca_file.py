f = open("data.txt", "r")
print(f.read())
f.close()

f = open("data.txt", "r")
for baris in f:
    print(baris.strip())
f.close()
