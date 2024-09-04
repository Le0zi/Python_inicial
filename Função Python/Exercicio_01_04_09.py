import os
import time

os.system("cls||clear")

def somar(n1:int, n2:int, qtd:int): 
    soma =n1 + n2 
    media=soma/qtd
    return  media

qtd=int(input("Informe quantidade "))
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
media = somar(num1, num2,qtd)#chamando a função somar, ela pode ser utilizada para facilitar a utilização de calculos de formas mutiplas utilizando apenas uma palavra
print(media)