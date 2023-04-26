
import funcoes
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql




def adm_tela():
    def usuario():
        main2.destroy()
        funcoes.tela_login()


    def tela():
        main4 = Tk()
        main4.title('tela adm')
        main4.mainloop()

    def login_adm():
        email = adm_email.get()
        senha = adm_senha.get()
        cpf = adm_cpf.get()
        con = sql.connect('db_greenway.db')
        db = con.cursor()
        db.execute(f"SELECT * FROM usuario WHERE email='{email}' AND senha='{senha}' AND [cpf/cnpj]='{cpf}'")
        resul = db.fetchall()
        if resul:
            messagebox.showinfo('Alert', 'Login feito com sucesso. Seja bem-vindo!')
            main2.destroy()
            tela()
        else:
            messagebox.showerror('ERROR', 'Erro de Login')

    main2 = Tk()
    main2.title('Administrador')
    main2.geometry('965x588+275+50')
    img_tela_adm = PhotoImage(file="imagens/telas/adm-tela.png")
    bt_usuario = PhotoImage(file="imagens/botoes/usuario-botao.png")
    bt_entrar = PhotoImage(file="imagens/botoes/entrar-botao.png")

    img_fundo2 = Label(main2, image=img_tela_adm)
    img_fundo2.pack()

    adm_email = Entry(main2, bd=2, font=("Montserrat", 15))
    adm_email.place(width=350, height=38.59, x=584, y=274.63)

    adm_cpf = Entry(main2, bd=2, font=("Montserrat", 15))
    adm_cpf.place(width=350, height=38.59, x=584, y=354)

    adm_senha = Entry(main2, show="*", bd=2, font=("Montserrat", 15))
    adm_senha.place(width=350, height=38.59, x=584, y=424.89)

    bot_usuario = Button(main2, bd=0, image=bt_usuario, command=usuario)
    bot_usuario.place(width=65, height=21, x=634, y=37)

    bot_entrar_adm = Button(main2, bd=0, image=bt_entrar, command=login_adm)
    bot_entrar_adm.place(width=126, height=45, x=681, y=493)
    main2.mainloop()



