# Monitoreo del consumo energético

##Desarrolle un programa que registre el consumo energético de cuatro edificios del campus 
##universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en 
##tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y 
##generar el promedio semanal correspondiente
 
# Defini las constantes
num_edificios = 4
dias_semana = 7
turnos_dia = 3

consumo_total = [0] * num_edificios

for edificio in range(num_edificios):
    print(f"\nedificio {edificio + 1}:") #Inicio del bucle
    for dia in range(dias_semana):
        print(f" dia {dia + 1}:")
        for turno in range(turnos_dia):
            while True:
                try:
                    consumo = float(input(f" Ingrese el comsumo en KWH {turno + 1}:"))
                    break
                except ValueError:
                    print(" Error, ingrese un numero valido")
            consumo_total[edificio] += consumo  # Bucle de los 3 trunos del dias

print("\nresumen del consumo semanal por edificio:")
for i in range(num_edificios):
    total = consumo_total[i]
    promedio = total / dias_semana
    print(f"edificio {i + 1} - total: {total:.2f} KMH, promedio diario: {promedio:.2f} KMH") # Mostrar el resultado
