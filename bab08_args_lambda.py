def jumlah_semua(*angka):
    return sum(angka)

def cetak_data(**data):
    for kunci, nilai in data.items():
        print(kunci, "=", nilai)

print(jumlah_semua(1, 2, 3, 4))
cetak_data(nama="Daffa", sekolah="SMKN 2 Subang")

kuadrat = lambda x: x * x
print(kuadrat(9))
