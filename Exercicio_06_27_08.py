import os
import time

pares=0
impares=0

for i in range(5):
    num = int(input("Informe o numero: "))
    time.sleep(1)
    if  num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares +1
print(f"Numeros pares: {pares}. \nNumeros impares: {impares}")