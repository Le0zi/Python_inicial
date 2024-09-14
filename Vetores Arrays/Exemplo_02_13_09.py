"""Crie um algoritmo que aciete apenas 6 valores
inteiros, positivos e pares, em seguida mostre na tela os 
valores lidos na ordem inversa.

Caso seja informado um numero diferente dos criterios apresentados acima, repita 
a pergunta para o usuario"""
import os 
import time

os.system("cls||clear")
QTD=10
num:int

def logo_senai(): #Criação da função
    os.system("cls||clear")#Conteudo da função
    print("""
          ==============
          --   SENAI  --
          ==============
          """)
    
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

logo_senai()
list = entrada()

#Resultado:
total=len(list)
logo_senai()
print("\n=== Resultado ===")
for i,numero in enumerate(reversed(list), start=1):
    print(f"{total-i+1}º numero: {numero}")    

