
from tkinter import *


janela = Tk()





bt1 = Button(janela, text= "ESTOQUE",width=30,command="")
bt2 = Button(janela, text= "CONSULTAS",width=30,command="")
bt3 = Button(janela, text= "VENDAS",width=30,command="")
bt5 = Button(janela, text= "CADASTRO FORNECEDOR",width=30,command="")
bt4 = Button(janela, text= "CADASTRO CLIENTE",width=30,command="")

bt1.place(x=100, y=50)
bt3.place(x=400, y=50)
bt5.place(x=100, y=150)
bt4.place(x=400, y=150)
bt2.place(x=270, y=250)


janela.geometry("700x300+400+400")
janela.mainloop()
