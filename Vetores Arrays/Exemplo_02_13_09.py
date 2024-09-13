"""Crie um algoritmo que aciete apenas 6 valores
inteiros, positivos e pares, em seguida mostre na tela os 
valores lidos na ordem inversa.

Caso seja informado um numero diferente dos criterios apresentados acima, repita 
a pergunta para o usuario"""
import os 
import time

os.system("cls||clear")
QTD=3
num:int

#Entrada:
def entrada ():
    list_num=[]
    for i in range (QTD):
        while True:
            num=int(input(f"{i+1}º numero: "))
            if (num>0) and (num %2==0):
                list_num.append(num)  
                break
            else:
                print("Numero incorreto, digite novamente...")
                time.sleep(1)
    return list_num

#Atribuição:
list = entrada()

#Resultado:
total=len(list)
print("\nAAAAAAAA")
for i,numero in enumerate(reversed(list), start=1):
    print(f"{total-i+1}º numero: {numero}")    

