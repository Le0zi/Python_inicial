"""
Escreva um algoritimo que solicite duas notas para um aluno.
caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
calcule e mostre a media aritimética do aluno.
"""
import os
import time
os.system ("cls||clear")
soma = 0 
quant = 3
for a in range (quant):
    while True:
        nota1=float(input(f"Informe a {a + 1}º nota: "))
        if (nota1<=0 or nota1>10):
            time.sleep(1)
            print("\nA nota dever ser maior ou igual a 0 e menor que ou igual a 10. ")
        else:
            break
    soma = nota1 + soma
media = soma/quant
print(f"Media: {media:.2f}")
