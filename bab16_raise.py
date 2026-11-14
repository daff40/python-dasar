def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif")
    return umur

try:
    cek_umur(-5)
except ValueError as e:
    print("Error:", e)

print(cek_umur(16))
