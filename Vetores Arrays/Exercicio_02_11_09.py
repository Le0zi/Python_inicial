"""Crie um programa que leia 3 notas, armazenando em um vetor e calcule a média aritimetrica.
Mostre as 3 notas informadas pelo usuario e informe a media."""

import os

os.system("cls||clear")

QTD = 6
list_nota=[]
soma=0

#Entrada de dados:

for i in range(QTD):
    nota=float(input(f"{i+1}ª Nota: "))
    list_nota.append(nota)     #Adicionando as notas na lista.

#Imprimindo dados:
for i, nota in enumerate(list_nota):
    soma +=nota
    print(f"{i+1}ª Nota: {nota}")

print(f"Media: {soma/QTD}")