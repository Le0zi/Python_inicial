"""Crie um programa que leia 3 notas, armazene em um vetor 
e mostre as notas informadas"""

import os

os.system("cls||clear")

list_notas=[]
QTD=3

#Solicitação de dados:
for i in range(QTD):
    nota=int(input(f"{i+1}ª nota: "))
    list_notas.append(nota)

#Imprimindo dados
for i, nota in enumerate(list_notas):
    print(f"{i+1}ª nota: {nota}")