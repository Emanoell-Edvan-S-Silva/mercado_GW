from tkinter import *
import random
from tkinter import messagebox

def codigo():
    a = random.randint(1000, 9999)
    print(a)
    def teste():

        b = int(a)
        t = en_codigo.get()
        z= int(t)
        if z == b:
            messagebox.showinfo('Alert', 'funcionou')
        else:
            messagebox.showinfo('ERROR', 'fedeu')


    master1 = Tk()
    master1.title('Confirme o código de redefinição')
    master1.geometry('965x588+275+50')
    master1.resizable(width=1, height=1)
    img_cod = PhotoImage(file="imagens/telas/codigo-senha.png")
    bt_prox = PhotoImage(file="imagens/botoes/proximo-senha.png")
    bt_cancel = PhotoImage(file="imagens/botoes/cancelar-senha.png")

    lab_tela = Label(master1, image=img_cod)
    lab_tela.pack()

    # Criação de caixas de entrada
    en_codigo = Entry(master1, bd=2, font=("Montserrat", 15))
    en_codigo.place(width=359, height=38.59, x=293, y=377)

    bot_prox = Button(master1, bd=0, image=bt_prox, command=teste)
    bot_prox.place(width=126, height=45, x=525, y=439)

    bot_cancel = Button(master1, bd=0, image=bt_cancel)
    bot_cancel.place(width=53, height=14, x=440, y=508)

    master1.mainloop()

codigo()