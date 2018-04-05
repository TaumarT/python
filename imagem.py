from tkinter import *

janela = Tk()

load = Image.open('mundial.jpg')
render = Image.PhotoImage(load)

img = Label( Image=render)
img.image = render
img.place(x=0, y=0)

janela.geometry("500x500+50+50")
janela.mainloop()