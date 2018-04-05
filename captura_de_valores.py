from tkinter import *
janela = Tk()
def bt_click():#função de capturar os numeros e somar

    #teste se o valor dos campos são numericos
    if(str(ed1.get()).isnumeric() and str(ed2.get())).isnumeric():
        primeiro_numero = int(ed1.get())
        segundo_numero = int(ed2.get())
        lb["text"] = primeiro_numero + segundo_numero
    else:
        lb["text"] = "Valores Invalidos"
        


janela.title("soma")

ed1 = Entry(janela)
ed1
ed2 = Entry(janela)
ed2.place(x=100, y= 130)

bt = Button(janela, text="soma", width=20, command=bt_click)
bt.place(x=100, y=150)
lb = Label(janela, text=" ")
lb.place(x=100, y=200)

janela.geometry("400x300+200+200")
janela.mainloop()