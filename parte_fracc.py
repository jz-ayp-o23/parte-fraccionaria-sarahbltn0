"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Entradas
numero = float(input("Introduzca un número: "))

# Proceso
if numero - int(numero) > 0:
    salida = "Sí tiene decimales"
elif numero - int(numero) == 0:
    salida = "No tiene decimales"

print(salida)