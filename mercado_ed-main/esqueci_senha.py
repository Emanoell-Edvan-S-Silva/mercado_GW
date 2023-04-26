from tkinter import *

def redefinir_senha():
    def codigo():
        def confirmar_senha():
            def volta():
                master2.destroy()
                codigo()

            master1.destroy()
            master2 = Tk()
            master2.title('Crie sua nova senha')
            master2.geometry('965x588+275+50')
            master2.resizable(width=1, height=1)
            img_confir = PhotoImage(file="imagens/telas/confirmar-senha.png")
            bt_redefine = PhotoImage(file="imagens/botoes/redefinir-senha.png")
            bt_cancela = PhotoImage(file="imagens/botoes/cancelar-senha.png")

            lab_tela = Label(master2, image=img_confir)
            lab_tela.pack()

            # Criação de caixas de entrada
            en_senha = Entry(master2, bd=2, font=("Montserrat", 15))
            en_senha.place(width=361, height=38.59, x=291, y=300)

            en_conf_senha = Entry(master2, bd=2, font=("Montserrat", 15))
            en_conf_senha.place(width=361, height=38.59, x=291, y=377)

            bot_redef = Button(master2, bd=0, image=bt_redefine)
            bot_redef.place(width=126, height=45, x=407, y=442)

            bot_cancela = Button(master2, bd=0, image=bt_cancela, command=volta)
            bot_cancela.place(width=53, height=14, x=440, y=508)

            master1.mainloop()

        def voltai():
            master1.destroy()
            redefinir_senha()

        master.destroy()
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

        bot_prox = Button(master1, bd=0, image=bt_prox, command=confirmar_senha)
        bot_prox.place(width=126, height=45, x=525, y=439)

        bot_cancel = Button(master1, bd=0, image=bt_cancel, command=voltai)
        bot_cancel.place(width=53, height=14, x=440, y=508)

        master1.mainloop()


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

    bot_proximo = Button(master, bd=0, image=bt_proximo, command=codigo)
    bot_proximo.place(width=126, height=45, x=402, y=449)

    bot_cancelar = Button(master, bd=0, image=bt_cancelar)
    bot_cancelar.place(width=53, height=14, x=440, y=508)

    master.mainloop()

redefinir_senha()