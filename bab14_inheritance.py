class Bentuk:
    def luas(self):
        return 0

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

class Lingkaran(Bentuk):
    def __init__(self, r):
        self.r = r

    def luas(self):
        return 3.14 * self.r ** 2

for b in [Persegi(4), Lingkaran(10)]:
    print(b.luas())
