"""Escreva um algoritimo que leia três  notas de um aluno.
Caso seja menor que - ou maior que 10, mostre a pergunta novamente

Após receber as notas dentro dos parâmetros acima, calcule a media verifique se o aluno está  
aprovado, recuperação ou reprovado considerando os seguintes criterios

Se media for a partir de 7, aprovado;
Se media for entre 5 e 6.9, o aluno está em recuperação;
Caso seja menor que 5r, o aluno está reprovado."""

import os 
import time

os.system("cls||clear")

contador=0
nota1=0
MULT=3
ultrapassou_limite = False

for a in range(MULT):
    while True:
        nota=float(input(f"Informe a {a+1}º nota: "))
        contador = 1 + contador
        if nota<0 or nota>10:
            print("Informe sua nota novamente: ")
            if contador == 3:
                print("Muitas tentativas erradas.")
                ultrapassou_limite = True
                break
        else:
            break
    if ultrapassou_limite:
        break
    
    nota1 = nota+nota1
media = nota1/MULT
if media >= 7:
    print("Parabéns, você foi aprovado...")
    time.sleep(1)
    print("===FIM===")
elif media >= 5:
    print("""
    1- SIM
    2- NÂO
        """)
    opcao=input("De acordo com sua nota, você foi reprovado. \nVocê gostaria de efetuar a recuperação? ").upper()
    match (opcao):
        case "1"|"SIM":
            print("Sua recuperação está agendada para a proxima aula...")
            time.sleep(1)
            print("===FIM===")
        case "2"|"NÃO":
            print(f"Okay, então sua media final é {media}")
            time.sleep(1)
            print("===FIM===")
        case _:
            print("Opção invalida...")
else:
    print(f"Você foi reprovado, sua media é {media}")

