def cetak_suara(hewan):
    print(hewan.suara())

class Sapi:
    def suara(self):
        return "Moo"

cetak_suara(Sapi())

print(len("Daffa"))
print(len([1, 2, 3, 4]))
print(len({"a": 1, "b": 2}))
