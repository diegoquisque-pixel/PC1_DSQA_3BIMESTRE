
import pyfiglet
from colorama import init, Fore, Back, Style

init()

# Alonzo = Amarillo
titulo = pyfiglet.figlet_format("ALONZO")
print(titulo)
print(Fore.CYAN + titulo + Style.RESET_ALL)
print(Fore.YELLOW + "Texto en color ")
print("😹😹")
# tup.py
# DIEGO QUISQUE

# Generar el texto en forma de arte ASCII
titulo = pyfiglet.figlet_format("INTELAF")
print(titulo)

# Tupla que contiene los salarios de los empleados
salarios = (5500, 6200, 4800, 7100, 5900)

# Inicializamos la suma total
total = 0

# Recorremos la tupla y sumamos cada salario
for salario in salarios:
    total += salario

# Mostramos el total acumulado
print("\n💰 Total de salarios a pagar este mes: Q", total)