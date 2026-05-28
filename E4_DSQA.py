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

# Generar el texto en forma de arte ASCII
titulo = pyfiglet.figlet_format("INTELAF")
print(titulo)

# Definimos tuplas con los nombres de empleados presentes por día
lunes = ("Ana", "Luis", "Carlos")
martes = ("Ana", "Sofía", "Luis")
miercoles = ("Carlos", "Luis", "Marta")
jueves = ("Ana", "Carlos", "Sofía")
viernes = ("Luis", "Marta", "Sofía")

# Solicitamos al usuario el nombre del empleado a revisar
nombre = input("\n👤 Ingrese el nombre del empleado para revisar su asistencia: ")

# Inicializamos el contador de días presente
presente = 0

# Verificamos si el empleado estuvo presente cada día
if nombre in lunes:
    presente += 1
if nombre in martes:
    presente += 1
if nombre in miercoles:
    presente += 1
if nombre in jueves:
    presente += 1
if nombre in viernes:
    presente += 1

# Mostramos cuántos días asistió el empleado
print(f"\n✅ {nombre} asistió {presente} días esta semana.")