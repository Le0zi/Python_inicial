import os
import time
os.system("cls||clear")
verificação=True
login:str
senha:str
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
def logando(login, senha):
    logo_senai()
    while True:
        contador =0
        login1=input("Informe seu usuario: ")
        if login1==login:
            carregamento()
            os.system("cls||clear")
            senha1=input("Informe sua senha: ")
            if senha1 == senha:
                carregamento()
                time.sleep(1)
                os.system("cls||clear")
                print("Login efetuado")
                break
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
def dados_salvos1():
    login = 'Leonardo'
    return login
def dados_salvos():
    senha= '12345'
    return senha
while True:
    logo_senai()
    opcao=int(input("""=========== Seja bem vindo:  ===========  
            1- Criar login
            2- Efetuar Login
            3-Sair do sistema
    Informe a opção desejada: """))
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
            login=dados_salvos1()
            senha=dados_salvos()
            logando(login, senha)
            break
        case 3:
            logo_senai()
            carregamento()
            os.system("cls||clear")
            logo_senai()
            print("Operação concluida")
            os.system("cls||clear")
        case _:
            pass
            break
