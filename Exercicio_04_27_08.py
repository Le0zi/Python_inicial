import os
import time

os.system("cls||clear")

num=int(input("Informe um numero que deseja fazer a contagem regressiva: "))

for i in range(num,0,-1):
    print(i)
    time.sleep(1)
print("===FIM===")