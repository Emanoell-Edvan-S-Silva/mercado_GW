from login_adm import *
from Cadastro_Usuario import *
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql


def tela_login():
    def tela():
        main4 = Tk()
        main4.title('tela')
        main4.mainloop()

    def login_bd():
        cpf = en_cpf.get()
        email = en_email.get()
        senha = en_senha.get()
        con = sql.connect('db_greenway.db')
        db = con.cursor()
        db.execute(f"SELECT * FROM usuario WHERE email='{email}' AND senha='{senha}' AND [cpf/cnpj]='{cpf}'")
        resul = db.fetchall()
        if resul:
            messagebox.showinfo('Alert', 'Login feito com sucesso. Seja bem-vindo!')
            main.destroy()
            tela()
        else:
            messagebox.showerror('ERROR', 'Erro de Login')

    def cadas():
        main.destroy()
        cadas_tela()

    def adm():
        main.destroy()
        adm_tela()

    # Importar imagens
    main = Tk()
    main.title('Greenway Supermercado')
    main.geometry('965x588+275+50')  # largura x altura + dist esquerda + dist topo
    main.resizable(width=1, height=1)
    bt_entrar = PhotoImage(file="imagens/botoes/entrar-botao.png")
    bt_cadas = PhotoImage(file="imagens/botoes/criar-ct-botao.png")
    bt_adm = PhotoImage(file="imagens/botoes/adm_botao.png")
    # bt_esqueci = PhotoImage(file="imagens/botoes/esqueci-senha-botao.png")
    img_f = PhotoImage(file="imagens/telas/log-tela.png")
    lab_tela = Label(main, image=img_f)
    lab_tela.pack()

    # Criação de caixas de entrada
    en_email = Entry(main, bd=2, font=("Montserrat", 15))
    en_email.place(width=350, height=38.59, x=584, y=264.63)

    en_cpf = Entry(main, bd=2, font=("Montserrat", 15))
    en_cpf.place(width=350, height=38.59, x=584, y=346)

    en_senha = Entry(main, show="*", bd=2, font=("Montserrat", 15))
    en_senha.place(width=350, height=38.59, x=584, y=421.89)

    # Criação de botões
    bot_entrar = Button(main, bd=0, image=bt_entrar, command=login_bd)
    bot_entrar.place(width=126, height=45, x=684, y=513)

    bot_cadas = Button(main, bd=0, image=bt_cadas, command=cadas)
    bot_cadas.place(width=141, height=19, x=781, y=196)

    bot_adm = Button(main, bd=0, image=bt_adm, command=adm)
    bot_adm.place(width=122, height=21, x=775, y=37)
    #
    # bot_esqueci = Button(main, bd=0, image=bt_esqueci, command=redefinir_senha)
    # bot_esqueci.place(width=120, height=14, x=767, y=483)

    main.mainloop()
