class Orang:
    def __init__(self, nama, alamat, saldo):
        self.nama = nama
        self._alamat = alamat
        self.__saldo = saldo

o = Orang("Daffa", "Subang", 500)
print(o.nama)
print(o._alamat)
print(o._Orang__saldo)

try:
    print(o.__saldo)
except AttributeError:
    print("Atribut private tidak bisa diakses langsung")
