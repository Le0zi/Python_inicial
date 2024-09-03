"""Crie um programa que ajude um usuário a controlar seus gastos 
mensais. O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido. O programa deve 
exibir o total gasto e o valor  excedente."""
import os
import time

os.system("cls||clear")

soma=0
limite_gast=float(input("Informe qual limite desejado: "))

while True:
    while True:
        gasto_diario=float(input("informe o valor do gasto: "))
        soma = gasto_diario + soma
        if soma == 0:
            print("saindo...")        
        elif soma>limite_gast:
            print("informe outro valor: ")
    opcao=int(input("""Desja inserir outro gasto ?\n1- SIM \n2-NÂO\n:"""))
    if soma > limite_gast:
        print("====Valor excedido====")
        break
    elif opcao == 2:
        print("===FIM===")
        break
    
