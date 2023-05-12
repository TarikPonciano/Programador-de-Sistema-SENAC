
from Controle.classConexao import Conexao
from customtkinter import *

conexaoBanco = Conexao("Biblioteca", "localhost",
                       "5432", "postgres", "postgres")
set_appearance_mode("dark")

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Cadastro de Livros")
        self.geometry("800x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.fonteTitulo = CTkFont(size=32, weight="bold")
        self.fontePadrao = CTkFont(size=24, weight="normal")

        self.tituloSuperior = CTkLabel(master=self, text="Tela de Cadastro de Livros", font=self.fonteTitulo)
        self.tituloSuperior.grid(column=0, row=0, padx = 20, pady = 20)

        self.formularioCadastroLivros = FormularioCadastro(self)
        self.formularioCadastroLivros.grid(column=0, row=1, padx=20, pady=20, sticky="nsew")

class FormularioCadastro(CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master=master, border_color="red", corner_radius=10)

        self.fonteTitulo = CTkFont(size=32, weight="bold")
        self.fontePadrao = CTkFont(size=24, weight="normal")

        self.grid_columnconfigure((1), weight= 1)

        self.rotuloNome = CTkLabel(master=self, text="Nome", font=self.fontePadrao)
        self.rotuloNome.grid(column=0, row=0, padx=(30,50), pady=(20,40))

        self.inserirNome = CTkEntry(master=self, placeholder_text="Insira o nome do Livro")
        self.inserirNome.grid(column=1, row=0, padx=(0,150), pady=(20,40),sticky="ew")

        self.rotuloAutor = CTkLabel(master=self, text="Autor", font=self.fontePadrao)
        self.rotuloAutor.grid(column=0, row=1, padx=(30,50), pady=(20,40))

        self.inserirAutor = CTkEntry(master=self, placeholder_text="Insira o nome do Autor")
        self.inserirAutor.grid(column=1, row=1, padx=(0,150), pady=(20,40),sticky="ew")

        self.inserirLivro = CTkButton(master=self, text="Enviar", command=self.inserirLivroNoBanco)
        self.inserirLivro.grid(column=1,row=3, padx=(0,200), pady=(20,0))

        self.rotuloResultado = CTkLabel(master=self)
        self.rotuloResultado.grid(column=1, row=4, padx=(0,200), pady=20)

    def inserirLivroNoBanco(self):
        nomeLivro = self.inserirNome.get()
        autorLivro = self.inserirAutor.get()

        if not nomeLivro or not autorLivro:
            self.rotuloResultado.configure(text="Digite as informações", text_color="red")

        else:
            if(conexaoBanco.manipularBanco(f'''
            INSERT INTO "Livros"
            Values(default,'{nomeLivro}','{autorLivro}')
            
            ''')):
                self.rotuloResultado.configure(text="Livro inserido com sucesso", text_color="green")

            else:
                self.rotuloResultado.configure(text="Houve um erro ao inserir o livro", text_color="red")




app = App()

app.mainloop()

