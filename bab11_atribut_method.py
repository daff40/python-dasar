class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

p = PersegiPanjang(5, 3)
print("Luas:", p.luas())
print("Keliling:", p.keliling())
p.lebar = 4
print("Luas baru:", p.luas())
