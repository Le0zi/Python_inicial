import os
import time

os.system("cls||clear")


def multiplicacao(n1):
    for i in range(1,11):
        mult=i*n1
        time.sleep(1)
        return mult
n1=int(input("Informe um  numero: "))
result=multiplicacao(n1)
print(result)