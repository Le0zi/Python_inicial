"""Crie um programa que, utilizando um laço `for`, calcule
 a soma dos números de 1 a 5 e mostre o resultado.
"""
import os 
import time 
os.system ("cls||clear")

soma=0

for i in range(1,5):
    soma = i + soma
    print(soma)
    time.sleep(1)
