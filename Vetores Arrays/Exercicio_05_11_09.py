"""Crie um programa que leaia 6 numeros, armazenados em um 
vetor  e informe quantos são pares e quantos impares.
Mostre os números informados pelo usuário."""
import os
os.system("cls||clear")

QTD=6
list_num=[]

#Entrada de dados:

for i in range(QTD):
    num=int(input(f"{i+1}° Numero: "))
    list_num.append(num)

#Processando:

def verificação(numeros):
    contador_par=0
    contador_impar=0
    for numero in numeros :
        if numero %2==0:
            contador_par+=1
            print("Leo")
        else:
            contador_impar+=1
            print("jeu")
    print(f"\Impares: {contador_impar} \nPares: {contador_par}")

resultado = verificação(list_num)

os.system("cls||clear")

#Exibindo dados:

print("=== Resultado ===\n")

print(resultado)