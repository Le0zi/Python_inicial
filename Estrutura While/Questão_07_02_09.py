"""Crie um programa que solicite ao usuário criar uma senha. O programa deve 
então pedir para confirmar a senha e garantir que ambas as senhas coincidam. Se as senhas 
não coincidirem, o programa deve continuar
pedindo para o usuário inserir e confirmar a  tenha até que ambas sejam iguais."""
import os 
import time

os.system("cls||clear")
contador = 0
senha=input("Crie uma senha: ")

while True:
    print("Confirmação de senha.")
    time.sleep(1)
    confirmacao=input("Confirmação: ")
    if confirmacao==senha:
        print("Senha confirmada com sucesso...")
        break
    else:
        print("Erro de confirmação, informe novamente...")
        contador += 1
        if contador ==5:
            print("Tentativas excedidas. ")