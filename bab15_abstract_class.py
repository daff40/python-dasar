from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        print("Meong")

class Anjing(Hewan):
    def suara(self):
        print("Guk guk")

Kucing().suara()
Anjing().suara()

try:
    h = Hewan()
except TypeError:
    print("Class abstrak tidak bisa dibuat objeknya")
