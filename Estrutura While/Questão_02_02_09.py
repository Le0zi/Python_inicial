"""Escreva um programa que use um laço while para encontrar o
 primeiro número maior que 50 que seja divisível por 7.
 Exiba esse número."""
import os
import time

os.system("cls||clear")

while True:
    num=int(input(f"Informe um numero: "))
    for i in range(num, 50,-1):
        if (i>50) and ( i % 7== 0):
            print(f"Numero: {i}")
            time.sleep(1)

