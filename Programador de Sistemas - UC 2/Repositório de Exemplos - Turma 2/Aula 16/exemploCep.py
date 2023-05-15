from customtkinter import *
import requests

class App(CTk):

    def __init__(self):
        super().__init__()

        self.title("Consulta CEP")

        self.geometry("600x600")

        self.columnconfigure(1, weight=1)

        self.tituloSuperior = CTkLabel(self, text="Cadastro de endereço")
        self.tituloSuperior.grid(column=0, row=0, columnspan=3, sticky="ew")

        self.rotuloCep = CTkLabel(self, text="CEP: ")
        self.rotuloCep.grid(column=0, row=1, padx=20, pady=20)

        self.inputCep = CTkEntry(self,placeholder_text="Digite seu CEP")
        self.inputCep.grid(column=1, row=1, padx=20, pady=20)

        self.consultaCep = CTkButton(self, text="Consultar", command=self.consultarCep)
        self.consultaCep.grid(column=2, row=1, padx=20, pady=20)

        self.rotuloLogradouro = CTkLabel(self, text="Logradouro: ")
        self.rotuloLogradouro.grid(column=0, row=2, padx=20, pady=(100,20))

        self.inputLogradouro = CTkEntry(self,placeholder_text="Digite seu Logradouro")
        self.inputLogradouro.grid(column=1, row=2, padx=20, pady=(100,20), sticky="ew")

        self.rotuloBairro = CTkLabel(self, text="Bairro: ")
        self.rotuloBairro.grid(column=0, row=3, padx=20, pady=20)

        self.inputBairro = CTkEntry(self,placeholder_text="Digite seu Bairro")
        self.inputBairro.grid(column=1, row=3, padx=20, pady=20, sticky="ew")

        self.rotuloCidade = CTkLabel(self, text="Cidade: ")
        self.rotuloCidade.grid(column=0, row=4, padx=20, pady=20)

        self.inputCidade = CTkEntry(self,placeholder_text="Digite sua Cidade")
        self.inputCidade.grid(column=1, row=4, padx=20, pady=20, sticky="ew")

        self.rotuloEstado = CTkLabel(self, text="Estado: ")
        self.rotuloEstado.grid(column=0, row=5, padx=20, pady=20)

        self.inputEstado = CTkOptionMenu(self,values=["BH","CE","PR"])
        self.inputEstado.grid(column=1, row=5, padx=20, pady=20, sticky="ew")

    def consultarCep(self):

        cep = self.inputCep.get()

        try:

            requisicao = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

            endereco = requisicao.json()

            self.inputLogradouro.delete('0','end')
            self.inputBairro.delete('0','end')
            self.inputCidade.delete('0','end')
            

            self.inputLogradouro.insert('end', endereco['logradouro'])

            self.inputBairro.insert('end', endereco['bairro'])

            self.inputCidade.insert('end', endereco['localidade'])

            self.inputEstado.set(endereco['uf'])

        except(Exception, requests.ConnectionError, requests.JSONDecodeError) as error:
            print(error)


if __name__ == "__main__":
    app = App()
    app.mainloop()