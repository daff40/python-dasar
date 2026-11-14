class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def sapa(self):
        print(f"Halo, saya {self.nama} dari jurusan {self.jurusan}")

m1 = Mahasiswa("Daffa", "RPL")
m2 = Mahasiswa("Budi", "TKJ")
m1.sapa()
m2.sapa()
