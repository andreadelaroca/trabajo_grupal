# Este programa registra la asistencia de estudiantes en tres secciones durante cinco días de la semana.
# Los datos se recopilan a través de la entrada del usuario y se calculan los totales por sección y el total general.

# Inicialización de variables para almacenar las asistencias
asistencias = 0
asistencias_seccion1 = 0
asistencias_seccion2 = 0
asistencias_seccion3 = 0
asistencias_total = 0
# números con los días de la semana
dia = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes"
}

# Bucle para iterar sobre los días de la semana
for i in range(1, 6):
    print(f"Registro de asistencia del {dia[i]}")
    # Bucle para iterar sobre los estudiantes de cada sección
    for j in range(1, 7):
        if j == 1 or j >= 0:
            # Registro de asistencia para la Sección 1
            while True:
                print(f"Sección 1 - Estudiante {j}:")
                try:
                    asistencia = int(input("¿Asistió? (1: Sí, 0: No): "))
                    if asistencia in [0, 1]:
                        asistencias_seccion1 += asistencia
                        break
                    else:
                        print("Por favor, ingrese solo 1 (Sí) o 0 (No).")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese solo 1 (Sí) o 0 (No).")
            
            # Registro de asistencia para la Sección 2
            while True:
                print(f"Sección 2 - Estudiante {j}:")
                try:
                    asistencia = int(input("¿Asistió? (1: Sí, 0: No): "))
                    if asistencia in [0, 1]:
                        asistencias_seccion2 += asistencia
                        break
                    else:
                        print("Por favor, ingrese solo 1 (Sí) o 0 (No).")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese solo 1 (Sí) o 0 (No).")
            
            # Registro de asistencia para la Sección 3
            while True:
                print(f"Sección 3 - Estudiante {j}:")
                try:
                    asistencia = int(input("¿Asistió? (1: Sí, 0: No): "))
                    if asistencia in [0, 1]:
                        asistencias_seccion3 += asistencia
                        break
                    else:
                        print("Por favor, ingrese solo 1 (Sí) o 0 (No).")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese solo 1 (Sí) o 0 (No).")
        else:
            print("Error")

# Cálculo del total de asistencias
asistencias_total += asistencias_seccion1 + asistencias_seccion2 + asistencias_seccion3

# Impresión de los resultados finales
print(f"Total de asistencias Sección 1: {asistencias_seccion1}")
print(f"Total de asistencias Sección 2: {asistencias_seccion2}")
print(f"Total de asistencias Sección 3: {asistencias_seccion3}")
print(f"Total de asistencias de la semana: {asistencias_total}")
