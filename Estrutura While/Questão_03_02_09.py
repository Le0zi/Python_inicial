"""Escreva um programa que multiplique um número inicial por um fator dado pelo usuário até que o produto exceda 100. Exiba o 
produto final e o número de multiplicações realizadas."""
import os
import time

os.system("cls||clear")

contador=0

while True:
    num=int(input("Informe o numero: "))
    for i in range(1,100):
        mult = num * i
        if mult > 100:
            print(f"{i} Excedeu")
            time.sleep(1)
            contador +=1
            if contador == 10:
                break
        
        
        