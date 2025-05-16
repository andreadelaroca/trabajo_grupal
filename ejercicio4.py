# monitoreo del consumo energético
# registrar el consumo energético de cuatro edificios del campus a lo largo de una semana.
# por cada día se ingresarán los kilovatios (kW) consumidos en tres turnos.
# calcular el consumo total por edificio y el promedio semanal.

import time

print("Monitoreo del consumo energético de cuatro edificios en UAM a lo largo de una semana")

# definición de variables iniciales
consumo_total_edificio = 0 # variable para almacenar el consumo total por edificio
consumo_total_semanal = 0 # variable para almacenar el consumo total semanal
consumo_diario = 0 # variable para almacenar el consumo diario
consumo_turno = 0 # variable para almacenar el consumo por turno
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] # lista de días
turnos = ["Mañana", "Tarde", "Noche"] # lista de turnos

# bucle para cada edificio
for edificio in range(1,6):
    print(f"\nEdificio No. {edificio}") # imprime el edificio que se está procesando
    time.sleep(1)
    consumo_total_edificio = 0  # Acumula el consumo del edificio actual
    
    # bucle para cada día de la semana
    for dia in dias:
        print(f"\nDía {dia}") # imprime el día que se está procesando
        time.sleep(0.8)
        
        # bucle para cada turno
        for turno in turnos:
            print(f"\nTurno de {turno}") # imprime el turno que se está procesando
            # bucle para validar el consumo
            while True: 
                try:
                    consumo_turno = float(input(f"Ingrese el consumo en kW para el turno de {turno}: "))
                    if consumo_turno < 0: # validación del consumo
                        print("El consumo no puede ser negativo. Intente nuevamente.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")
            consumo_diario += consumo_turno
            print(f"El consumo en el turno de {turno} fue de {consumo_turno}kW") # imprime el consumo por turno
            time.sleep(0.6)
            
        # suma el consumo del turno al consumo diario
        print(f"\nConsumo total del día {dia}: {consumo_diario}kW")
        consumo_total_edificio += consumo_diario # suma el consumo diario al total del edificio
        time.sleep(1)
        
    # al finalizar la semana, se imprime el consumo total del edificio
    print(f"\nConsumo total del edificio {edificio}: {consumo_total_edificio}kW") # imprime el consumo total del edificio
    consumo_total_semanal += consumo_total_edificio # suma el consumo total del edificio al total semanal
    time.sleep(1.5)
    
# al finalizar la semana, se imprime el consumo total semanal
print(f"\nConsumo total de todos los edificios en la semana: {consumo_total_semanal}kW")
promedio_semanal = consumo_total_semanal / 5 #calcula el promedio semanal
print(f"\nPromedio de consumo semanal por edificio: {promedio_semanal:.2f}kW") # imprime el promedio semanal
