"""Crie um programa que ajude um estudante a calcular a média de 
suas notas. O programa deve permitir que o usuário insira notas de provas até que o usuário 
insira um valor 
negativo. O programa deve calcular e exibir a média das notas inseridas."""
import os
import time 

os.system("cls||clear")

quant_nt: str
soma=0

while True:
    quant_nt=int(input("Quantas notas deseja adcionar ? "))
    for i in range(quant_nt):
        nota=float(input(f"{i+1}º Nota: "))
        if nota>=0:
            soma+=nota
        else:
            break
    break
print(f"Media: {soma/quant_nt}")