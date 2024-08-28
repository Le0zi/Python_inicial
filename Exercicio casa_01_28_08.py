import os 
import time

os.system("cls||clear")

nota1=0
mult=4

for a in range(mult):
    while True:
        nota=float(input(f"Informe a {a+1}º nota: "))
        if nota<0 or nota>10:
            print("Informe sua nota novamente: ")
        else:
            break
    nota1 = nota+nota1
media = nota1/mult
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

