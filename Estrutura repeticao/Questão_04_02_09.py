"""Escreva
um programa que use um laço `for` 
para exibir a tabuada do 2, de 2 até 20."""

import os
import time
os.system("cls||clear")

numero=2

for i in range(11):
    mult = numero * i
    print(f"{numero}x{i} = {mult}")
    time.sleep(1)
