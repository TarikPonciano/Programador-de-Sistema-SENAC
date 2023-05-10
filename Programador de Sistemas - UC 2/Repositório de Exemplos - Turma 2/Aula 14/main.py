#Recursos

# Repositório Oficial - https://github.com/TomSchimansky/CustomTkinter
# Site Oficial (Documentação) - https://customtkinter.tomschimansky.com/
# Playlist tutorial em português - https://www.youtube.com/watch?v=hIJ6sf0x3Yw&list=PL6KTZQDPGs5gZYtK9YblxA-Te9wQM8mdb 

#Objetivos

# - Criar uma janela
# - Colocar texto nessa janela
# - Modificar o texto na janela utilizando um input
# - Criar um formulário de inserção
# - Integrar o formulário com o banco de dados
# - Criar um menu

from customtkinter import * #pip install customtkinter

app = CTk()
app.title("Teste")
larguraJanela = 800
alturaJanela = 600
app.geometry(f"{larguraJanela}x{alturaJanela}")

app.grid_columnconfigure((0), weight=1)


tituloTopo = CTkLabel(master=app, text= "Olá Mundo!", text_color="red", font=CTkFont(size=36,weight="bold"))
tituloTopo.grid(row=0,column=0, padx=20, pady=20)

corpoDoTexto = CTkLabel(master=app, text="Este é meu programa!", font=CTkFont(size=36))
corpoDoTexto.grid(row=1, column=0, padx=20, pady = 20)


app.mainloop()
