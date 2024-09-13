"""Crie um algoritimo que receba do usuário valores e armazene em 
um vetor 5 números, caso seja informado um valor negativo, atribua o valor zero.
- Liste os valores do vetor"""




#Entrada:

QTD=5
lista_num=[]
for i in range (QTD):
    num=int(input(f"{i+1}º numero: "))
    lista_num.append(num)


#Verificação:

def verificacao (a):
    lista_1=[]
    for num in a:
        if num <0:
            num = 0
            lista_1.append(num)
        else:
            lista_1.append(num)

    return lista_1

#Exibindo dados:

resultado = verificacao(lista_num)

for i,numero in enumerate(resultado):
    print(f"{1+i}º Numero: {numero}")