import funcoes
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
#
# from funcoes import tela_login


def cadas_tela():

        #função para cadastrar
    def cadastro():
        reg_nomecomp = regis_nome.get() + ' ' + regis_sobrenome.get()
        reg_email = regis_email.get()
        reg_senha = regis_senha.get()
        reg_cpf = regis_cpf.get()

        if reg_nomecomp == '':
            messagebox.showerror('ERROR', 'Nome inválido') #nome vazio
        elif reg_email == '':
            messagebox.showerror('ERROR', 'Email inválido!') #email vazio
        elif reg_senha == '':
            messagebox.showerror('ERROR', 'Senha inválida!') #senha vazia
        elif reg_cpf == '':
            messagebox.showerror('ERROR', 'CPF/CNPJ inválido!')  # CPF vazio
        else:
            con = sql.connect('db_greenway.db')
            db = con.cursor()
            db.execute(f"INSERT INTO usuario (nome_completo, email, senha, [cpf/cnpj]) Values ('{reg_nomecomp}', '{reg_email}', '{reg_senha}', '{reg_cpf}')")
            con.commit()
            messagebox.showinfo('ALERT', 'Registro feito com sucesso.')
            main1.destroy()
            funcoes.tela_login()

#função para voltar
    def voltar():
        main1.destroy()
        funcoes.tela_login()

    main1 = Tk()
    main1.title('Cadastre-se')
    main1.geometry('965x588+275+50')
    img_tela_cad = PhotoImage(file="imagens/telas/cad-tela.png")
    bt_cadas1 = PhotoImage(file="imagens/botoes/cad-botao.png")
    bt_log_voltar = PhotoImage(file="imagens/botoes/fazer-log-botao.png")

    img_fundo1 = Label(main1, image=img_tela_cad)
    img_fundo1.pack()

    regis_nome = Entry(main1, bd=2, font=("Montserrat", 12))
    regis_nome.place(width=164, height=31, x=531, y=208)

    regis_sobrenome = Entry(main1, bd=2, font=("Montserrat", 12))
    regis_sobrenome.place(width=164, height=31, x=716, y=208)

    regis_email = Entry(main1, bd=2, font=("Montserrat", 12))
    regis_email.place(width=349, height=31, x=531, y=267)

    regis_cpf = Entry(main1, bd=2, font=("Montserrat", 12))
    regis_cpf.place(width=349, height=31, x=531, y=330)

    regis_senha = Entry(main1, show="*", bd=2, font=("Montserrat", 12))
    regis_senha.place(width=349, height=31, x=531, y=388)

    bot_log_voltar = Button(main1, bd=0, image=bt_log_voltar, command=voltar)
    bot_log_voltar.place(width=141, height=19, x=707, y=437)

    bot_cadas1 = Button(main1, bd=0, image=bt_cadas1, command=cadastro)
    bot_cadas1.place(width=212, height=45, x=601, y=486)
    main1.mainloop()


