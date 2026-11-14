class Kucing:
    def suara(self):
        return "Meong"

class Anjing:
    def suara(self):
        return "Guk guk"

class Bebek:
    def suara(self):
        return "Kwek kwek"

for hewan in [Kucing(), Anjing(), Bebek()]:
    print(hewan.suara())
