from tkinter import *
def bt_click():
    # função para alterar o texto  da label

    lb["text"] = ed.get()

janela = Tk()
janela.title("taian taumar")
janela["background"] = "white"
ed = Entry(janela, width = 50)
ed.place(x=200, y=200)
#L*A+E+T
janela.geometry("600x600")#tamanho da janela
lb = Label(janela, text="Hello Word!")#texto que esta  contido na janela
lb.place(x=250, y=250)#pozicionamento do texto na tela coordenadas X e Y
bt = Button(janela, width=20, text = "OK",command=bt_click )
bt.place(x= 300, y=300)#pozicionamento do  botão na tela coordenadas X e Y
janela.mainloop()