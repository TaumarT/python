#Tela_de_Login.py
from tkinter import *


janela = Tk()
janela.title("Mundial Quimica")
def logar():

	login = ed1.get()
	senha = ed2.get()

	if(login == "taian") and (senha == "1234"):
		import Mundial_Quimica
		Mundial_Quimica.Tela_de_Login()
		#lb["text"] = "Usuario Logado"
	else:
		lb["text"] = "Valores Invalidos"


lb1 = Label(janela, text = "login: ")
lb2 = Label(janela, text="senha: ")

ed1 = Entry(janela,)
ed2 = Entry(janela,show='*')

bt1 = Button(janela, text= "confirmar",width=10,command=logar)
lb1.place(x= 40, y=50)
lb2.place(x= 40, y=80)
ed1.place(x= 80, y=50)
ed2.place(x= 80, y=80)
bt1.place(x=100, y=150)
lb = Label(janela, text=" ")
lb.place(x=100, y=200)

janela.geometry("300x300+400+400")
janela.mainloop()
