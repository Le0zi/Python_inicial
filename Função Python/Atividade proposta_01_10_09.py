import os
import time 
os.system("cls||clear")

DIAAT=11
MESAT=9
ANOAT=2024
segundos = 0
minutos = 0
horas = 0
dia = 0 
mes = 0
ano = 0
while True:
    for i in range(60):
        segundos = i + 1
        time.sleep(0.01)
        print(f"Ano: {ano}, Mês: {mes},Dia: {dia}, Horas: {horas}, Min: {minutos}, Seg: {segundos}")
        if segundos ==60:
            minutos +=1
            os.system("cls||clear")
            if minutos == 60:
                horas+=1
                minutos -=60
                os.system("cls||clear")
                if horas == 24:
                    dia +=1
                    horas -=24
                    os.system("cls||clear")
                    if dia == 30:
                        mes +=1
                        dia -=29
                        os.system("cls||clear")
                        if mes==12:
                            ano+=1
                            mes -=11
                            os.system("cls||clear")
