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


# Generar el texto en forma de arte ASCII
titulo = pyfiglet.figlet_format("INTELAF")
print(titulo)

# Tupla que contiene las opciones del menú como pares (código, descripción)
menu_soporte = (
    ("1", "Ver tickets abiertos"),
    ("2", "Registrar nuevo ticket"),
    ("3", "Cerrar ticket"),
    ("4", "Salir del sistema")
)

# Título del sistema
print("\n🛠️ Menú de Soporte Técnico")

# Mostramos cada opción usando un ciclo
for codigo, descripcion in menu_soporte:
    print(f"{codigo}. {descripcion}")

# Iniciamos un bucle para que el usuario interactúe
while True:
    # Solicitamos una opción
    opcion = input("\nSeleccione una opción (1-4): ")

    # Evaluamos cada opción usando condicionales
    if opcion == "1":
        print("📋 Mostrando tickets abiertos...")
    elif opcion == "2":
        print("📝 Iniciando registro de nuevo ticket...")
    elif opcion == "3":
        print("✅ Ticket cerrado correctamente.")
    elif opcion == "4":
        print("👋 Saliendo del sistema. ¡Gracias!")
        break  # Salimos del bucle
    else:
        print("❌ Opción inválida. Intente nuevamente.")