"""Crie uma função que receba um numero e mostre uma mensagem
informando se o numero é par ou impar"""

import os

os.system("cls||clear")
contador = 0
contador2 = 0

def impar_par(n1:int, contador:int, contador2:int):
    for i in range(6):   
        num1=int(input("Informe um numero: "))
        if n1%2==0:
            print("Par")
            contador+=1
        else:
            print("Impar")
            contador2+=1
    print(f"Quantidade pares {}")

