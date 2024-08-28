import os 
import time

os.system("cls||clear")

media = 0
media1= media/4
for i in range(4):
    nota = int(input(f"Informe a {i+1}º nota: "))
    media = media + nota
for i in range(10000):
    if media1 > 6:
        print("Você foi aprovada")
        print("""
        1 - SIM
        2 - NÂO
          """)
        opcao=int(input("Gostaria de saber sua media ? "))
        time.sleep(2)
        match(opcao):
            case 1:
                print(f"Sua media é {media1}")
            case 2:
                print("===FIM===")
            case _:
                print("Opção invalida...")
    elif media1>=4:
        print("Você foi reprovado")
        print("""
        1 - SIM
        2 - NÂO
          """)
        opcao=int(input("Gostaria fazer recuperação ? "))
        time.sleep(1)
        match(opcao):
            case 1:
                print(f"Sua recuperação está agendada, e sua media atual é {media1}")
            case 2:
                print("===FIM===")
            case _:
                print("Opção invalida...")
    else:
        print("Você foi reprovado")
        print("""
        1 - SIM
        2 - NÂO
          """)
        opcao=int(input("Gostaria de informar que você \nnão tem direito a recuperação, gostaria de saber sua media! "))
        time.sleep(1)
        match(opcao):
            case 1:
                print(f"Sua media é {media1}")
            case 2:
                print("===FIM===")
            case _:
                print("Opção invalida...")
