

import os
os.system("cls||clear")

def inflacao(num:float):
    if num<100:
        numif = num+(num*0.1)
    else:
        numif = num+(num*0.2)
    return numif
    


produto=float(input("Informe o valor do produto: "))
valor=inflacao(produto)
print(f"Valor inflacionado: {valor}R$")