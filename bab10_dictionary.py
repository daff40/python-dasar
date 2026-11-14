siswa = {"nama": "Daffa", "kelas": "XI RPL", "umur": 16}
print(siswa)
print(siswa["nama"])
print(siswa.get("sekolah", "tidak ada"))

siswa["sekolah"] = "SMKN 2 Subang"
siswa["umur"] = 17
del siswa["kelas"]
print(siswa)
print(len(siswa))
