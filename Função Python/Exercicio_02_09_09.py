import os

os.system("cls||clear")
def logo_senai():
    print("""
        ===============
          
        ---- SENAI ----
          
        ===============
           """)
def solicitacao_peso():
    peso=float(input("Peso: "))
    return peso
def solicitacao_altura():
    altura=float(input("Altura: "))
    return altura
def IMC ():
    while True:
        print("**********************")
        peso = solicitacao_peso()
        altura = solicitacao_altura()
        print("**********************")
        imc=peso/(altura*altura)
        if imc<18.5:
            print("Abaixo do peso:\nConsulte um nutricionista para orientação.")
        elif imc<=24.9:
            print("Peso normal:\nMantenha habitos saudáveis.")
        elif imc<=29.9:
            print("Sobrepeso:\nConsidere uma dieta e atividade fisica.")
        elif imc <=34.9:
            print("Obesidade Grau I:\nProcure orientação de um profissional.")
        elif imc<=39.9:
            print("Obesidade Grau II:\nConsulte um medico para avaliação e orientação.")
        else:
            print("Obesidade Grau III:\nBusque assistência media imediatamente")
logo_senai()
IMC()
os.system("cls||clear")
logo_senai()
