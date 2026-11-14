class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup")

rek = BankAccount(1000)
rek.setor(500)
print(rek.get_saldo())
rek.tarik(300)
print(rek.get_saldo())
rek.tarik(5000)
