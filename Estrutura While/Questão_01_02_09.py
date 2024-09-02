""" Desenvolva um programa que conte quantos números negativos foram 
inseridos pelo usuário usando um laço while. O programa deve parar quando o usuário 
inserir 0 ou um número positivo. Mostre a quantidade de números negativos."""
import os 
import time
contador =0
os.system("cls||clear")
while True:
    num=float(input("Informe um numero: "))
    if (num<0):
            print("...")
    else:
        print("Não permitido numero positivos e zero...")
        print(f"O numero incorreto foi {num}")
        break
    contador +=1
print(f"{contador} numeros negativos foram adcionados.")
            
            
