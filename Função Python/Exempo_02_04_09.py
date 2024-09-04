import os
import time

os.system("cls||clear")

def somar(n1:int, n2:int):
    soma =n1 + n2
    return soma #Retornando resultado da função

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

soma = somar(num1, num2)#chamando a função somar, ela pode ser utilizada para facilitar a utilização de calculos de formas mutiplas utilizando apenas uma palavra
print(soma)