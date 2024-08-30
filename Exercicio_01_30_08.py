import os
import time

os.system("cls||clear")

soma=0
contador_certo=0
limite=False
contador = 0

print("""N para nova nota ou S para terminar\n 
1- N
2- S
    """)
opcao=input("Deseja inserir mais uma nota? ").upper()

match (opcao):
    case "1"|"S":
        q_nota =int(input("Informe a quantidade de notas que deseja inserir: "))
        for i in range(q_nota):
            while True:
                nota=float(input(f"Informe a {i+1}º nota: "))
                if (nota<0) or (nota>10):
                    print("Nota invalida. \nInforme uma nota entre 0 e 10...")
                    contador = contador + 1
                    if contador == 3:
                        contador = contador +1
                        limite=True
                        break
                else:
                    contador_certo = contador + 1
                    soma += nota
                    break
            if limite:
                break    
        media = soma /q_nota
        print(f"Media: {media}") 
        time.sleep(1)
        print(f"Houveram {contador_certo} de tentativas certas, e {contador} de tentativas erradas.")     
    case "2"|"N":
        print("Muito obrigado por usar nosso sistema.")
    case _:
        print("Opção invalida")