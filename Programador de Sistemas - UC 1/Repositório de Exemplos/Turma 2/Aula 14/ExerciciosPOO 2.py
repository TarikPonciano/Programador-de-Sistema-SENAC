class Agenda:
    def __init__(self,listaDeContatos, maxContatos):

        self.listaDeContatos = listaDeContatos
        self.maxContatos = maxContatos

    def adicionarContato(self, novoContato):
        if len(self.listaDeContatos) < self.maxContatos:
            self.listaDeContatos.append(novoContato)
        else:
            print("Contato não foi adicionado. Limite atingido.")
        

    def removerContato(self,nomeContato):
        for contato in self.listaDeContatos:
            if contato.nome == nomeContato:
                self.listaDeContatos.remove(contato)


    def informacoes(self):
        
        impressaoLista = ""

        for contato in self.listaDeContatos:
            impressaoLista = impressaoLista + f"• {contato.nome} - {contato.telefone} \n"
        return impressaoLista


class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


contato1 = Contato("Jorge","1o23-123i9-123")

contato2 = Contato("Maicou", "1230140819841982")

contato3 = Contato("Maria", "1231151512")

minhaAgenda = Agenda([contato1,contato2,contato3], 5)

print(minhaAgenda.informacoes())

minhaAgenda.removerContato("Maria")

print(minhaAgenda.informacoes())

minhaAgenda.adicionarContato(Contato("Josuel", "1231411"))

minhaAgenda.adicionarContato(Contato("Milena", "1231412e121"))

print(minhaAgenda.informacoes())

minhaAgenda.adicionarContato(Contato("Fabricio","12312d12e1"))

minhaAgenda.adicionarContato(Contato("Pericles", "1djoi1jd12"))

