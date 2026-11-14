try:
    angka = int("42")
except ValueError:
    print("Gagal konversi")
else:
    print("Berhasil:", angka)
finally:
    print("Blok finally selalu dijalankan")
