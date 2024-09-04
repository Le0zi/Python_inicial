import os
import time

os.system("cls||clear")

def descontos_salario(salario_bruto:float):
    vale_transporte=200
    vale_refeição=100
    plano_de_saude=300
    resultado = salario_bruto-(vale_transporte+vale_refeição+plano_de_saude)
    return resultado   #

salario_bruto=float(input("Informe o salario bruto: "))
salario_liquido=descontos_salario(salario_bruto)
print(f"{salario_liquido}R$")
