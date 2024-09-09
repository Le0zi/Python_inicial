


import os

os.system("cls||clear")

#Entrada
def entrada():
    quant_not=3
    soma=0
    for i in range(quant_not):
        while True:
            nota=float(input(f"Digite a {i+1}° nota: "))
            if nota >= 0 and nota<=10:
                print("")
                soma+=nota
                break
            else:
                print("Nota incorreta...")
        media = soma/quant_not
    return media


def verificacao():
    media = entrada()
    if media >=7:
        print("aprovado")
        print(f"Media: {media}")
    else:
        print("Reprovado")
        print(f"Media: {media}")

verificacao()
