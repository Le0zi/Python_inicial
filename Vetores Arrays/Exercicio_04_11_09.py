"""Crie um programa que leia 5 numeros, armazenando em um e informe qual maior numero e qual o menor.
Mostre os numeros informados pelo usuario."""

import os 
os.system("cls||clear")

QTD=5
list_num=[]

#Entrada de dados:

for i in range(QTD):
    numero=int(input(f"{1+i}° Numero: "))
    list_num.append(numero)

#Processamento:
def Saida (numero):
    maior=max(list_num)
    menor=min(list_num)
    print(f"\nMenor numero: {menor}")
    print(f"\nMaior numero: {maior}")

resultado = Saida(list_num)


#Saida de dados:
for i, numero in enumerate(list_num):
    print(f"{i+1}° Numero: {numero}")
print("\n=== Resultado ===\n")
print(resultado)
    