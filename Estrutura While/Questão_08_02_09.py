"""Crie um programa para ajudar o usuário a acompanhar suas 
metas de estudo. O usuário define uma meta de horas de estudo e o programa deve 
permitir que o usuário insira o número de horas estudadas até que o total atinja ou 
exceda a meta. O programa deve  exibir o total de horas estudadas e o valor excedente.
"""

import os
import time

os.system("cls||clear")
horas_total=0
horas=float(input("Informe a quantidade de horas para a meta.\n-> "))

while True:
    for i in range(horas):
        horas_dia =("Já estudadas: \n")
        horas_total+=horas_dia
        diferenca = horas - horas_total
    if horas_total>horas_dia:
        print(f"Excedeu as horas. \nValor excedido: {diferenca}")