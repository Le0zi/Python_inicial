"""Desenvolva um programa que solicite ao usuário inserir um código 
de promoção para obter um desconto. O código correto é "PROMO2024". O usuário tem 3 tentativas para acertar
o código. Se o código estiver correto, exiba uma mensagem de "Código aceito" e o desconto. Se o usuário 
errar o código nas 3 tentativas, exiba uma mensagem de Código inválido"""
import os
import time

os.system("cls||clear")
codigo ="PROMO2024"
contador=0
while True:
    codigo1=input("Informe o codigo promocional: ").upper()
    if codigo1 == codigo:
        print("===Codigo aceito===")
        break
    elif codigo1 != codigo:
        contador+=1
        if contador ==3:
            time.sleep(1)
            print("Codigo Invalido...")
            break