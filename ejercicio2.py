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
# Función para crear los estados de las computadoras (ocupada o libre)
def crear_estado():
    estado = []
    for i in range(FILAS):
        fila = [] 
        for j in range(COLUMNAS):
            ocupada = random.choice([True, False]) # Simular ocupación aleatoria
            fila.append(ocupada) 
        estado.append(fila)
    return estado
# Función para mostrar el estado de las computadoras
print ("X = Ocupada")
print ("O = Libre")
def mostrar_estado(estado, nombre_laboratorio):
    print(f"\nEstado de {nombre_laboratorio}:")
    for fila in estado:
        for computadora in fila:
            if computadora:
                print("X", end=" ")  # end = "" se trata para dejarlo en una sola linea
            else:
                print("O", end=" ")  #  end = "" se trata para dejarlo en una sola linea
        print()
# Función para contar cuántas están ocupadas y cuántas libres
def contar_computadoras(estado):
    ocupadas = 0
    for fila in estado:
        for computadora in fila:
            if computadora:
                ocupadas += 1 
    libres = FILAS * COLUMNAS - ocupadas
    return ocupadas, libres
# Programa principal
def main():
    estado1 = crear_estado() #Crear el estado de las computadoras
    estado2 = crear_estado() 
    mostrar_estado(estado1, LABORATORIOS[0]) #Mostrar el estado de las computadoras
    mostrar_estado(estado2, LABORATORIOS[1])
    ocupadas1, libres1 = contar_computadoras(estado1)# Contar cuántas están ocupadas y cuántas libres
    ocupadas2, libres2 = contar_computadoras(estado2)
# Resumen general del trabajo
    print("\nResumen de computadoras:")
    print(f"Total de computadoras en {LABORATORIOS[0]}: {FILAS * COLUMNAS}") #Laboratorio 1
    print(f"Total de computadoras en {LABORATORIOS[1]}: {FILAS * COLUMNAS}") #Laboratorio 2
    print ("*" * 50)
    print(f"--Resumen de {LABORATORIOS[0]}: {ocupadas1} ocupadas, {libres1} libres") #Resumen de computadoras
    print(f"--Resumen de {LABORATORIOS[1]}: {ocupadas2} ocupadas, {libres2} libres") 

    # Ejecutar el programa
    
main()
