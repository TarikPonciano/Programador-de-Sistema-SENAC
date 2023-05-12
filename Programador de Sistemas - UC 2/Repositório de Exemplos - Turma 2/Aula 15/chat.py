
from customtkinter import *
from functools import partial

class App(CTk):

    def __init__(self):
        super().__init__()

        self.title("Meu chat")

        self.geometry("800x600")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.caixaDeMensagem = CTkTextbox(master=self,fg_color="gray", state="disabled", font=CTkFont(size=32), text_color="black")
        self.caixaDeMensagem.grid(column=0,row=0, padx = 30, pady = 30, sticky="nsew")

        self.widgetEnvioMensagem = CTkFrame(master=self,fg_color="black")
        self.widgetEnvioMensagem.grid(column=0, row=1, padx= 30,pady=(0,30), sticky="nsew")
        self.widgetEnvioMensagem.columnconfigure(1, weight=1)

        self.campoNome = CTkEntry(master=self.widgetEnvioMensagem, placeholder_text="Digite seu nome")
        self.campoNome.grid(column=0, row=0, padx=30, pady=10)

        self.campoMensagem = CTkEntry(master=self.widgetEnvioMensagem, placeholder_text="Digite sua mensagem")
        self.campoMensagem.grid(column=1, row=0, padx=30, pady=10, sticky="ew")
        self.campoMensagem.bind("<Return>",command=self.inserirTextoNaCaixa)

        self.botaoEnviar = CTkButton(master=self.widgetEnvioMensagem, text="Enviar", bg_color="blue", command=self.inserirTextoNaCaixa)
        self.botaoEnviar.grid(column=2, row=0, padx=30, pady=10)
    
    def inserirTextoNaCaixa(self, *args, **kwargs):

        nome = self.campoNome.get()

        mensagem = self.campoMensagem.get()

        resultado = f"{nome}: {mensagem}\n"

        self.caixaDeMensagem.configure(state = "normal")

        self.caixaDeMensagem.insert("end",resultado)

        self.caixaDeMensagem.configure(state = "disabled")

        self.campoMensagem.delete(0,"end")




app = App()

app.mainloop()
