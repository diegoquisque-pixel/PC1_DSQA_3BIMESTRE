import pyfiglet
from colorama import init, Fore, Back, Style

init()

# Alonzo = Amarillo
titulo = pyfiglet.figlet_format("ALONZO")
print(titulo)
print(Fore.YELLOW + titulo + Style.RESET_ALL)
print(Fore.RED + "Texto en color ")
print("😹😹")

# tup.py
# DIEGO QUISQUE

# Tuplas en Python

import pyfiglet

# Generar el texto en forma de arte ASCII
titulo = pyfiglet.figlet_format("INTELAF")
print(titulo)

# Creamos una tupla de tuplas, cada una con nombre y precio de producto
productos = (("Laptop", 6500), ("Monitor", 1800), ("Teclado", 250), ("Mouse", 120))

# Mostramos título del listados
print("\n📋 Lista de productos tecnológicos disponibles:")

# Recorremos la tupla principal con un ciclo
for producto, precio in productos:
    # Imprimimos cada producto con su precio formateado
    print(f"- {producto}: ${precio}")