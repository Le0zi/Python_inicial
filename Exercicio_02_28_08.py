"""
Escreva um algoritimo que solicite duas notas para um aluno.
caso seja menor que 0 ou maior que 10, mostre a pergunta novamente.
calcule e mostre a media aritimética do aluno.
"""
import os
import time
os.system ("cls||clear")

while True:

    nota1=float(input("Informe a primeira nota: "))
    nota2=float(input("Informe a segunda nota: "))

    if (nota1<=0 or nota1>10) or (nota2<0 or nota2>10):
        time.sleep(1)
        print("\nA nota dever ser maior ou igual a 0 e menor que ou igual a 10. ")
    else:
        break
media = (nota1+nota2)/2
print(f"Sua primeira nota é {nota1} e a segunda é {nota2}, e a media é {media}")
