class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(self.nama, "sedang makan")

class Burung(Hewan):
    def terbang(self):
        print(self.nama, "sedang terbang")

b = Burung("Elang")
b.makan()
b.terbang()
