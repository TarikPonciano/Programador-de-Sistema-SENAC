class Livro:
    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco

    def getPreco(self):
        return self.preco

    def setPreco(self, novoPreco):
        self.preco = novoPreco

livro1 = Livro("aspokaops", 20, "aosas", 50)
print(livro1.getPreco())
livro1.setPreco(30)
print(livro1.getPreco())