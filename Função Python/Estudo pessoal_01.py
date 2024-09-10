import os 
os.system("cls||clear")

def logo_senai():
    print("""
===============
---  SENAI  ---
===============          

""")
def IMC (peso:float,altura:float):
    while True:
        imc=peso/(altura*altura)
        if imc<18.5:
            print("Abaixo do peso:\nConsulte um nutricionista para orientação.")
            break
        elif imc<=24.9:
            print("Peso normal:\nMantenha habitos saudáveis.")
            break
        elif imc<=29.9:
            print("Sobrepeso:\nConsidere uma dieta e atividade fisica.")
            break
        elif imc <=34.9:
            print("Obesidade Grau I:\nProcure orientação de um profissional.")
            break
        elif imc<=39.9:
            print("Obesidade Grau II:\nConsulte um medico para avaliação e orientação.")
            break
        else:
            print("Obesidade Grau III:\nBusque assistência media imediatamente")  
            break
        
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
logo_senai()
opcao=int(input("""Informe a opção desejada:\n
                1-Calculo de IMC
                2-Calculadora
                :"""))
os.system("cls||clear")
match (opcao):
    case 1:
        logo_senai()
        peso=float(input("Peso: "))
        altura=float(input("Altura: "))
        resultado=IMC(peso, altura)
        print(resultado)
    case 2:
        logo_senai()
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
    case _:
        pass