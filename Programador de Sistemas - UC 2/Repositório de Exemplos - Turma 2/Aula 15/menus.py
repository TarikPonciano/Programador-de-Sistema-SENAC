from customtkinter import *
from Controle.classConexao import Conexao
from functools import partial

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Gerenciamento")
        self.geometry("800x600")

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)


        #Menu de navegação
        self.menuNavegacao = CTkFrame(self, fg_color="gray")
        self.menuNavegacao.grid(column=0, row=0, sticky="nsew")

        self.menuNavegacao.columnconfigure(0, weight=1)
    
        self.botaoTelaInicial = CTkButton(self.menuNavegacao, text="Tela Inicial", command=partial(self.abrirTela,"Tela Inicial"))
        self.botaoTelaInicial.grid(column=0,row=0, padx= 20, pady= 25)

        self.botaoInserirLivro = CTkButton(self.menuNavegacao, text="Inserir Livro", command=partial(self.abrirTela,"Inserir Livro"))
        self.botaoInserirLivro.grid(column=0, row=1, padx= 20, pady= 25)

        self.botaoVisualizarLivros = CTkButton(self.menuNavegacao, text="Visualizar Livros", command=partial(self.abrirTela,"Visualizar Livros"))
        self.botaoVisualizarLivros.grid(column=0, row=2, padx= 20, pady= 25)


        #Tela Inicial
        self.telaInicial = CTkFrame(self, fg_color="black")
        self.telaInicial.grid(column=1, row=0, sticky="nsew")

        self.telaInicial.columnconfigure(0, weight=1)
        self.telaInicial.rowconfigure(0,weight=1)

        self.mensagemBoasVindas = CTkLabel(self.telaInicial, text="Bem vindo ao Sistema de Gerenciamento SG",text_color="white",font=CTkFont(size=32,weight="bold"), compound="center", wraplength=300)
        self.mensagemBoasVindas.grid(column=0,row=0, sticky="nsew")

        #Tela Inserir Livro

        self.telaInserirLivro = CTkFrame(self, fg_color="transparent")

        self.tituloInserirLivro = CTkLabel(self.telaInserirLivro, text= "Inserir Livro", font=CTkFont(size=32))
        self.tituloInserirLivro.grid(column=0, row=0)

        self.rotuloNome = CTkLabel(self.telaInserirLivro, text= "Nome: ", font=CTkFont(size=32))
        self.rotuloNome.grid(column=0, row=1, padx=30, pady=30) 

        self.campoNome = CTkEntry(self.telaInserirLivro, placeholder_text=("Digite o nome do Livro"))
        self.campoNome.grid(column=1, row=1, padx= 10, pady = 30)

        self.rotuloAutor = CTkLabel(self.telaInserirLivro, text= "Autor: ", font=CTkFont(size=32))
        self.rotuloAutor.grid(column=0, row=2, padx=30, pady=30) 

        self.campoAutor = CTkEntry(self.telaInserirLivro, placeholder_text=("Digite o nome do Autor"))
        self.campoAutor.grid(column=1, row=2, padx= 10, pady = 30)

        self.botaoInserirLivro = CTkButton(self.telaInserirLivro, text="Enviar", command=self.inserirLivroBanco)
        self.botaoInserirLivro.grid(column=0, row=3)

        #Tela Visualizar Livros

        self.telaVisualizarLivros = CTkFrame(self, fg_color="transparent")
        self.telaVisualizarLivros.grid_columnconfigure(0,weight=1)
        self.telaVisualizarLivros.grid_rowconfigure(1,weight=1)

        self.tituloVisualizarLivros = CTkLabel(self.telaVisualizarLivros, text= "Lista de Livros", font=CTkFont(size=32))
        self.tituloVisualizarLivros.grid(column=0, row=0)

        self.listaDeLivros = CTkTextbox(self.telaVisualizarLivros, fg_color="black", text_color="white")
        self.listaDeLivros.grid(column=0, row =1, sticky="nsew")

        

    def inserirLivroBanco(self):

        conexaoBanco = Conexao("Biblioteca", "localhost",
                       "5432", "postgres", "postgres")
        
        nome = self.campoNome.get()

        autor = self.campoAutor.get()

        conexaoBanco.manipularBanco(f'''
        Insert into "Livros"
        values(default, '{nome}', '{autor}') 
        ''')
        

    def abrirTela(self,nomeDaTela):

        if nomeDaTela == "Tela Inicial":
            self.telaInicial.grid(column=1,row=0, sticky="nsew")
        else:
            self.telaInicial.grid_forget()

        if nomeDaTela == "Inserir Livro":
            self.telaInserirLivro.grid(column=1,row=0, sticky="nsew")
        else:
            self.telaInserirLivro.grid_forget()

        if nomeDaTela == "Visualizar Livros":
            self.telaVisualizarLivros.grid(column=1,row=0, sticky="nsew")
            conexaoBanco = Conexao("Biblioteca", "localhost",
                       "5432", "postgres", "postgres")
        
            livros = conexaoBanco.consultarBanco('''Select * From "Livros"
            Order BY "Nome" ASC ''')

            textoExibicao = "ID | Nome | Autor \n"

            for livro in livros:

                textoExibicao += f"{livro[0]} | {livro[1]} | {livro[2]} \n"

            self.listaDeLivros.insert("end", textoExibicao)

        else:
            self.telaVisualizarLivros.grid_forget()
            self.listaDeLivros.delete("0.0","end")





if __name__ == "__main__":
    app = App()
    app.mainloop()