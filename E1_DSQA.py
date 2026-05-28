# tup.py
# DIEGO QUISQUE
# Tuplas en Python

import pyfiglet
from colorama import init, Fore, Back, Style

init()

# Alonzo = Amarillo
titulo = pyfiglet.figlet_format("ALONZO")
print(titulo)
print(Fore.YELLOW + titulo + Style.RESET_ALL)
print(Fore.RED + "Texto en color ")
print("😹😹")

# Creamos una tupla con los nombres de empleados autorizados
empleados_autorizados = ("Ana", "Carlos", "Luis", "Marta", "Sofía")

# Mensaje de bienvenida al sistema
print("🔒 Verificación de acceso al sistema")

# Solicitamos el nombre del usuario
nombre = input("Ingrese su nombre: ")

# Verificamos si el nombre está dentro de la tupla
if nombre in empleados_autorizados:
    # Si está, damos acceso
    print(f"✅ Acceso concedido a {nombre}")
else:
    # Si no está, denegamos acceso
    print("❌ Acceso denegado. Usuario no autorizado.")