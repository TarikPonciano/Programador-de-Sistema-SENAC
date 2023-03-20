class Livro:
    def __init__(self, nome, qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco
    
    def getPreco(self):
        textoPreco = f"R$ {self.preco:.2f}"
        return textoPreco
    
    def setPreco(self, novoPreco):
        self.preco = novoPreco


livro1 = Livro("Senhor dos anéis", "99999", "Tolkien", 30)

print(livro1.getPreco())

livro1.setPreco(2000)

print(livro1.getPreco())