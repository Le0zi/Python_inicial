import os
os.system("cls|")
def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

num=int(input("Informe um numero:"))
resultado=tabuada(num)
print(resultado)