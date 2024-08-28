import os
import time
os.system("cls||clear")

soma=0

for i in range(4):
    nota=float(input(f"Informe a {i+1}º nota: "))
    soma = soma+nota
print(f"Sua media é {soma/4}")