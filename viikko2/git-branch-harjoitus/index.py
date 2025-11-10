# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{summa(x, y)}") #bugikorjaus
print(f"{erotus(x, y)}") #bugikorjaus

logger("lopetetaan")
print("goodbye!") # lisäys bugikorjaus-branchissa
