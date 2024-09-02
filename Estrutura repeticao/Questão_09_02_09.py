"""Desenvolva um programa que utilize dois laços `for` (um dentro do outro) para imprimir um retângulo de 
4 linhas por 6  colunas de asteriscos (`*`)."""

import os 
largura = "*"
altura="*"
espaco =" "
os.system("cls||clear")
contador =0
for i in range(1):
    print(largura*7)
    for i in range(5):
        print(altura, espaco,espaco,altura)   
        contador = contador +1
        if contador == 5:
            for i in range(1):
                print(largura*7)
        
   