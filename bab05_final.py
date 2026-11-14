from typing import Final

MAKS_SISWA: Final = 36
NAMA_APLIKASI: Final = "Praktikum Python"

print(MAKS_SISWA)
print(NAMA_APLIKASI)

# Final hanya petunjuk untuk editor, Python tetap mengizinkan perubahan
MAKS_SISWA = 40
print("Setelah diubah:", MAKS_SISWA)
