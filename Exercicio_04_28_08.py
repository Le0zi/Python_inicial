import os
import time
os.system("cls||clear")

login: str
senha: str
contador = 0

print("""
1- SIM
2- NÂO
      """)

opcao1=input("Deseja criar login ?").upper()

match (opcao1):
    case "1" | "SIM":
        login=input("Informe o login desejado: ")
        time.sleep(1)
        senha= input("Informe a senha desejada: ")
    case "2" | "NÂO":
        print("Só será possivel acesso, mediante apresentação de login e senha.")
    case _:
        print("Opção invalida")
time.sleep(1)
for a in range(1):
    while True:
        print("==== Efetue o login ====")
        time.sleep(1)
        login1=input("Login: ")
        contador +=1
        if login1!=login:
            print("Login incorreto, digite novamente.")
            if contador == 3:
                    break
        else:
            senha1=input("Senha: ")
            if senha1 != senha:
                print("Senha incorreta, tente novamente.")
                if contador == 3:
                    break
            else:
                print("===Login efetuado com sucesso===") 
                break
        
