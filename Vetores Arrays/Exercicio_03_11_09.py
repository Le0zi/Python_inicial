"""Faça um programa que leia 4 notas, armazenando em um vetor e calcule a media aritimética.
Verifique a situação do aluno fazendo algumas considerações:
-Media maior que 7: aprovado
-Media mair ou igual a 5: recuperação
-Media menor que 5: reprovado
 Mostre as 4 notas  informadas pelo usuario e informe a media."""
import os
os.system("cls||clear")

QTD=4
list_notas=[]
soma=0

def aprovação (media):
    if media>=7:
        print(f"Media: {media} Aprovado")
    elif media>=5:
        print(f"Media: {media} Recuperação")
    else:
        print(f"Media: {media} Reprovado")

#Entrada de dados:

for i in range (QTD):
    nota=float(input(f"{i+1}ª Nota: "))
    list_notas.append(nota)

#Processamento de dados:

for i, nota in enumerate(list_notas):
    soma+=nota
    media_ari=soma/QTD

#Saida de dados:

resultado =aprovação(media_ari)
print(resultado)