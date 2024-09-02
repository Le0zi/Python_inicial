"""Escreva um programa que utilize um laço for para multiplicar
 cada número de 1 a 6 por 3 e exibir o resultado."""

import os 
import time

os.system("cls||clear")

numero = 3

for i in range (1,7):
    mult= i * numero
    print(f"{numero} x {i} = {mult}")
    time.sleep(1)

