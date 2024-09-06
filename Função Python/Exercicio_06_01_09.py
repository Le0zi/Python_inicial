"""Crie uma função que receba um numero e mostre uma mensagem
informando se o numero é par ou impar"""

import os

os.system("cls||clear")

def impar_par():
    contador = 0
    contador2 = 0
    for i in range(6):   
        num1=int(input("Informe um numero: "))
        if num1%2==0:
            print("Par")
            contador+=1
        else:
            print("Impar")
            contador2+=1
    print(f"Quantidade Pares {contador}")
    print(f"Quantidade impares {contador2}")
impar_par()
