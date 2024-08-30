import os
import time
os.system("cls||clear")

q_nota: int
parte1=3
soma =0
nota1 = 0
for a in range(parte1):
    while True:
        nota=float(input(f"Informe a {a+1}º nota: "))
        if nota<0 or nota>10:
            print("Informe sua nota novamente: ")
        else:
            break
        nota1 = nota+nota1
media1 = nota1/parte1
time.sleep(1)

print(""""
1- Inserir mais uma nota (S)
2- Ver quantas notas foram inseridas (P) 
3- Calcular média aritimética das notas informadas
      """)
opcao=input("Informe a opção desejada: ").upper()

match (opcao):
    case "1"|"S":
        q_nota=int(input("Quantas notas novas deseja informar ?"))
        for a in range(q_nota):
            while True:
                nota=float(input(f"Informe a {a+4}º nota: "))
                if nota<0 or nota>10:
                    print("Informe sua nota novamente: ")
                else:
                    break
            soma = nota+soma
    case "2"|"P":
        quantidade_tt=q_nota+parte1
        print(f"{quantidade_tt} foram informadas")
    case "3"|"N":
        media = media1 + (soma/q_nota)
        print(f"Media: {media}")