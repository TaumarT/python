from tkinter import *
import sqlite3 

#Mundial_Quimica.py


janela = Tk()


janela.title("Mundial Quimica")


	#nome = Nome.get()
	#bairro = Bairro.get()
	#firma = firma.get()
	#endereco = endereco.get()
	#numero = numero.get()
	#cnpj = cnpj.get()
	#fone = fone.get()
	#celular = celular.get()
	#cidade = cidade.get()
	#cep = cep.get()
	#estado = estado.get()
	##inscricao_estadual = inscricao_estadual.get()
	#comprador =comprador.get()


nomel=Label(janela, text="Nome:")
nomel.place(x=60, y=50)
Nome = Entry(janela)
Nome.place(x=100, y=50)

bairrol = Label(janela, text="Bairro:")
bairrol.place(x=60, y=80)
Bairro = Entry(janela)
Bairro.place(x=100, y=80)

firmal=Label(janela, text="firma:")
firmal.place(x=60, y=115)
firma = Entry(janela)
firma.place(x=100, y=115)

enderecol=Label(janela, text="endereço:")
enderecol.place(x=40, y=150)
endereco = Entry(janela)
endereco.place(x=100, y=150)

numero1=Label(janela, text="numero:")
numero1.place(x=45, y=180)
numero = Entry(janela)
numero.place(x=100, y=180)

cnpj1=Label(janela, text="cnpj:")
cnpj1.place(x=65, y=210)
cnpj = Entry(janela)
cnpj.place(x=100, y=210)

fone1=Label(janela, text="fone:")
fone1.place(x=65, y=240)
fone = Entry(janela)
fone.place(x=100, y=240)


celular1=Label(janela, text="celular:")
celular1.place(x=55, y=270)
celular = Entry(janela)
celular.place(x=100, y=270)

cidade1=Label(janela, text="cidade:")
cidade1.place(x=55, y=300)
cidade = Entry(janela)
cidade.place(x=100, y=300)

cep1=Label(janela, text="CEP:")
cep1.place(x=70, y=330)
cep = Entry(janela)
cep.place(x=100, y=330)

estado1=Label(janela, text="estado:")
estado1.place(x=50, y=360)
estado = Entry(janela)
estado.place(x=100, y=360)

inscricao1=Label(janela, text="inscrição estadual:")
inscricao1.place(x=45, y=390)
inscricao_estadual = Entry(janela)
inscricao_estadual.place(x=150, y=390)

comprador1=Label(janela, text="comprador:")
comprador1.place(x=40, y=430)
comprador = Entry(janela)
comprador.place(x=110, y=430)

#data_emissao1=Label(janela, text="data emissão:")
#data_emissao1.place(x=40, y=460)
#data_emissao = Entry(janela)
#data_emissao.place(x=120, y=460)

#numero_fatura1=Label(janela, text="numero fatura:")
#numero_fatura1.place(x=40, y=490)
#numero_fatura= Entry(janela )
#numero_fatura.place(x=125, y=490)



#vencimento1=Label(janela, text="vencimento:")
#vencimento1.place(x=40, y=530)
#vencimento = Entry(janela)
#vencimento.place(x=110, y=530)



bt = Button(janela, text="confirmar")
bt.place(x=90, y=580)

#ed1 = Entry(janela)
#ed1.place(x=100, y=100)


janela.geometry("400x750")
janela.mainloop()
