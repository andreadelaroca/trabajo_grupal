# Ejercicio 2: Uso de computadoras en laboratorios
# Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del
# campus. 
# Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora
# se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con
# valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras
# ocupadas y libres por laboratorio.


import os
import random
os.system("cls || clear")  # Limpiar la pantalla
print ("**Bienvenidos a la UAM**")
LABORATORIOS = ["Laboratorio 1", "Laboratorio 2"] #Cantidad de Laboratorios
FILAS = 5
COLUMNAS = 4