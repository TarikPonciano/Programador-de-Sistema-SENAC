from Controle.classConexao import Conexao
from customtkinter import *

conexaoBanco = Conexao("Biblioteca", "localhost",
                       "5432", "postgres", "postgres")
set_appearance_mode("dark")

app = CTk()

fontePadrao = CTkFont(size=24,weight="bold")

app.title("Inserção de livro")

app.geometry("800x600")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=0)

def inserirLivroNoBanco():
    nomeLivro = insercaoNome.get()
    autorLivro = insercaoAutor.get()

    if not nomeLivro or not autorLivro:
        rotuloResultado.configure(text="Digite as informações", text_color="red")

    else:
        if(conexaoBanco.manipularBanco(f'''
        INSERT INTO "Livros"
        Values(default,'{nomeLivro}','{autorLivro}')
        
        ''')):
            rotuloResultado.configure(text="Livro inserido com sucesso", text_color="green")

            formularioInserirLivro.forget()
        else:
            rotuloResultado.configure(text="Houve um erro ao inserir o livro", text_color="red")

tituloInserirLivro = CTkLabel(master=app, font=CTkFont(size=36, weight="bold"), text="Tela de Cadastro de Livros")
tituloInserirLivro.grid(column=0, row=0, padx=20,pady=20)

formularioInserirLivro = CTkFrame(master=app,border_color="red", corner_radius=10)
formularioInserirLivro.grid(column=0, row=1, padx=10, pady=20, sticky="nsew")

formularioInserirLivro.grid_columnconfigure((1), weight= 1)

espacamentoRotuloHorizontal = (50,50)

rotuloNome = CTkLabel(master=formularioInserirLivro, text="Nome:", font=fontePadrao)
rotuloNome.grid(column=0,row=1, padx=espacamentoRotuloHorizontal, pady=20)

insercaoNome = CTkEntry(master=formularioInserirLivro, placeholder_text=("Digite o Nome"))
insercaoNome.grid(column=1, row=1, padx=(20,100), pady=20, sticky="ew")

rotuloAutor = CTkLabel(master=formularioInserirLivro, text="Autor:", font=fontePadrao)
rotuloAutor.grid(column=0,row=2, padx=espacamentoRotuloHorizontal, pady=20)

insercaoAutor = CTkEntry(master=formularioInserirLivro, placeholder_text=("Digite o Autor"))
insercaoAutor.grid(column=1, row=2, padx=(20,100), pady=20, sticky="ew")

inserirLivro = CTkButton(master=formularioInserirLivro, text="Enviar", command=inserirLivroNoBanco)
inserirLivro.grid(column=1,row=3, padx=(0,200), pady=(20,0))

rotuloResultado = CTkLabel(master=formularioInserirLivro)
rotuloResultado.grid(column=1, row=4, padx=(0,200), pady=20)

app.mainloop()

