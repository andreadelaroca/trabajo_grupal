asistencias = 0
asistencias_seccion1 = 0
asistencias_seccion2 = 0
asistencias_seccion3 = 0
asistencias_total = 0
dia = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes"
}
for i in range(1, 6):
    print(f"Registro de asistencia del {dia[i]}")
    for j in range(1, 7):
        if j == 1 or j >= 0:
            print(f"Sección 1 - Estudiante {j}:")
            while True:
                try:
                    print(f"Sección 1 - Estudiante {j}:")
                    asistencia = int(input("¿Asistió? (1: Sí, 0: No): "))
                    if asistencia in [0, 1]:
                        asistencias_seccion1 += asistencia
                        break
                    else:
                        print("Por favor, ingrese solo 1 (Sí) o 0 (No).")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese solo 1 (Sí) o 0 (No).")
            
            print(f"Sección 2 - Estudiante {j}:")
            while True:
                try:
                    asistencia = int(input("¿Asistió? (1: Sí, 0: No): "))
                    if asistencia in [0, 1]:
                        asistencias_seccion2 += asistencia
                        break
                    else:
                        print("Por favor, ingrese solo 1 (Sí) o 0 (No).")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese solo 1 (Sí) o 0 (No).")
            
            print(f"Sección 3 - Estudiante {j}:")
            while True:
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
asistencias_total += asistencias_seccion1 + asistencias_seccion2 + asistencias_seccion3
print(f"Total de asistencias Sección 1: {asistencias_seccion1}")
print(f"Total de asistencias Sección 2: {asistencias_seccion2}")
print(f"Total de asistencias Sección 3: {asistencias_seccion3}")
print(f"Total de asistencias de la semana: {asistencias_total}")
