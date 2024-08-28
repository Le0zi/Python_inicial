import os
import time
os.system("cls||clear")

soma=0

for i in range(4):
    nota=float(input(f"Informe a {i+1}º nota: "))
    soma = soma+nota
    time.sleep
media = soma/4

if media >7:
    print("Aprovado")
elif media>=4:
    print("Recuperação")
else:
    print("Reprovado")