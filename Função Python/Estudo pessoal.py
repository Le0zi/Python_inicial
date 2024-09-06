import os
import time
os.system("cls||clear")
verificação=True
login:str
senha:str
contador =0
def logo_senai():
    print("""
===============
---  SENAI  ---
===============          

""")
def criando_login():
    login=input("Crie seu usuario: ")
    senha=input("Crie sua Senha: ")
def carregamento():
    for i in range(1,1001):
        print(f"{i*0.1:.1f}%")
        time.sleep(0.001)
def logando():
    logo_senai()
    while True:
        login1=input("Informe seu usuario: ")
        if login1==login:
            carregamento()
            senha1=input("Informe sua senha: ")
            if senha1 == senha:
                carregamento()
                time.sleep(1)
                print("Login efetuado")
            else:
                contador +=1
                print("Login ou senha Incorretos, informe novamente")
                if contador==3:
                    break
        else:
            contador+=1
            print("Dados incorretos, informe novamente.")
            if contador ==3:
                break
def dados_salvos():
    login = 'Leonardo'
    senha = '2001'
    return senha, login
while True:
    logo_senai()
    opcao=int(input("""=========== Seja bem vindo:  ===========  
            1- Criar login
            2- Efetuar Login
            3-Sair do sistema
    Informe a opção desejada: """))
    carregamento()
    print("Carregamento efetuado sucesso.")
    time.sleep(1)
    os.system("cls||clear")
    match (opcao):
        case 1:
            criando_login()
            opcao2=input("""Deseja efetuar login ?
              1- SIM
              2- NÂO
            : """)
            match (opcao2):
                case "1"|"SIM":
                    carregamento()
                    print("Login efetuado.")
                case "2"|"NÂO":
                    carregamento
                    verificação=False
                    print("Sistema encerrado")
                    if verificação==False:
                        break
        case 2:
            dados_salvos()
            logando()