"""Crie um programa que ajude um usuário a controlar seus gastos 
mensais. O programa deve permitir que o usuário insira gastos diários até que o total gasto no mês exceda um orçamento inicial fornecido. O programa deve 
exibir o total gasto e o valor  excedente."""
import os
import time

os.system("cls||clear")

gasto=0

while True:
    max_gs=float(input("Informe o valor maximo de orçamento: "))
    print("""Deseja informar algum gasto ?\n
          1- SIM
          2-NÃO
          """)
    opcao=input("?").upper()

    match (opcao):
        case "1"| "SIM":
            while True:
                valor=float(input("Insira o valor: "))
                gasto += valor
        case "2"|"NAO":
            break
