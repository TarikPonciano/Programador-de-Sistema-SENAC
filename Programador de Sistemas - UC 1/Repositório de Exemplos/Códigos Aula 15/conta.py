class Conta:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def getTitular(self):
        return self._titular

    def setTitular(self, novoTitular):
        self._titular = novoTitular

    def getSaldo(self):
        return self._saldo

    def setSaldo(self, valor):
        self._saldo = valor

conta1 = Conta("João", 300)

print(conta1.getSaldo())
print(conta1.getTitular())

conta1.setSaldo(500)
conta1.setTitular("Maria")

print(conta1.getSaldo())
print(conta1.getTitular())


