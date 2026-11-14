class Akun:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo

    def lihat_saldo(self):
        return self.__saldo

a = Akun("Daffa", 1000)
print(a.pemilik)
print(a.lihat_saldo())
