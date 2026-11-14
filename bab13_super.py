class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")

class MahasiswaBaru(Mahasiswa):
    def __init__(self, nama, jurusan, angkatan):
        super().__init__(nama, jurusan)
        self.angkatan = angkatan

    def info(self):
        super().info()
        print("Angkatan:", self.angkatan)

mb = MahasiswaBaru("Daffa", "RPL", 2025)
mb.info()
