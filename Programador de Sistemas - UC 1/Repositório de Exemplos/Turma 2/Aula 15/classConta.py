class Conta:

    def __init__(self, saldo, numConta):
        self._saldo = saldo
        self._numConta = numConta
    
    def getSaldo(self):
        return self._saldo
    
    def setSaldo(self, novoSaldo):
        
        if novoSaldo < 0:
            print("Digite um saldo positivo")
        else:
            self._saldo = novoSaldo

    def getNumConta(self):
        return self._numConta
    
    def setNumConta(self, novoNumero):
        self._numConta = novoNumero