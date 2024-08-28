import os
import time

os.system("cls||clear")

soma=0

for i in range(5):
    num=int(input(f"Informe o {i+1}º numero: "))
    soma = soma + num
    time.sleep(1)
print(f"A soma dos numeros é {soma}...","\n===FIM===")