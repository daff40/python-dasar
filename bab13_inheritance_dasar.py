class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan bersuara")

class Kucing(Hewan):
    def suara(self):
        print(self.nama, "berkata: Meong")

class Anjing(Hewan):
    def suara(self):
        print(self.nama, "berkata: Guk guk")

Hewan("Hewan umum").suara()
Kucing("Tom").suara()
Anjing("Rex").suara()
