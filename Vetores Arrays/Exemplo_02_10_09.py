import os
os.system("cls||clear")

#Entrada:

lista_notas=[]

for i in range (2):
    nota = float(input(f"{1+i}° Nota:"))
    lista_notas.append(nota)

for nota in lista_notas:
    print(nota)