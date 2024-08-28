import os 
os.system("cls||clear")

while True:
    nota=float(input("Digite uma nota: "))

    if nota < 0 or nota>10:
        print("\nA nota dever ser maior ou igual a 0 e menor que ou igual a 10. ")
    else:
        break
print(f"nota: {nota}")
