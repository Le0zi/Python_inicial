"""Crie funções que recebam 2 numeros e retorne a soma, subtração, divisão e a m
ultiplicação destes dois numeros informados

obs: Crie uma função para cada operação"""

import os
os.system("cls||clear")
def opera(opcao:int,num1:float, num2:float):
    match (opcao):
        case 1: 
            resultado= num1+num2
        case 2:
            resultado= num1*num2
        case 3:
            resultado= num1-num2
        case 4:
            resultado=num1/num2
        case _:
            resultado = print("Opção invalida...")
    return resultado 
operacao = int(input("""Informe a operação:
                     1-Soma
                     2-Multiplicação
                     3-Subtração
                     4-Divisão
                     \n:"""))
numero1 = float(input("Informe um numero: "))
numero2 = float(input("Informe um numero: "))
resultado=opera(operacao, numero1,numero2)
print(resultado)