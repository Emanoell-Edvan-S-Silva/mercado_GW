from tkinter import *



def redefinir_senha():

    def email():
        email = en_email.get()
        print(email)

    master = Tk()
    master.title('Redefinir senha')
    master.geometry('965x588+275+50')
    master.resizable(width=1, height=1)
    img_redefinir = PhotoImage(file="imagens/telas/esqueci-senha.png")
    bt_proximo = PhotoImage(file="imagens/botoes/proximo-senha.png")
    bt_cancelar = PhotoImage(file="imagens/botoes/cancelar-senha.png")

    lab_tela = Label(master, image=img_redefinir)
    lab_tela.pack()

    # Criação de caixas de entrada
    en_email = Entry(master, bd=2, font=("Montserrat", 15))
    en_email.place(width=358, height=38.59, x=291, y=371)

    bot_proximo = Button(master, bd=0, image=bt_proximo, command=email)
    bot_proximo.place(width=126, height=45, x=402, y=449)

    bot_cancelar = Button(master, bd=0, image=bt_cancelar)
    bot_cancelar.place(width=53, height=14, x=440, y=508)

    master.mainloop()


redefinir_senha()

