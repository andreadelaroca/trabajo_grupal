# monitoreo del consumo energético
# registrar el consumo energético de cuatro edificios del campus a lo largo de una semana.
# por cada día se ingresarán los kilovatios (kW) consumidos en tres turnos.
# calcular el consumo total por edificio y el promedio semanal.

# definición de variables iniciales
consumo_total = 0 # variable para almacenar el consumo total de kW
consumo_semanal = 0 # variable para almacenar el consumo semanal de kW
consumo_diario = 0 # variable para almacenar el consumo diario de kW
consumo_turno = 0 # variable para almacenar el consumo por turno
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] # lista de días
turnos = ["Mañana", "Tarde", "Noche"] # lista de turnos

print("Monitoreo del consumo energético de cuatro edificios en UAM a lo largo de una semana")

# bucle para cada edificio
for edificio in range(1,6):
    print(f"\nEdificio No. {edificio}") # imprime el edificio que se está procesando
    # bucle para cada día de la semana
    for dia in dias:
        print(f"Día {dia}") # imprime el día que se está procesando
        # bucle para cada turno
        for turno in turnos:
            print(f"Turno de {turno}") # imprime el turno que se está procesando
            consumo_turno = float(input(f"Ingrese el consumo en kW: "))
            if consumo_turno < 0: # validación del consumo
                # si el consumo es negativo, se solicita nuevamente
                print("El consumo no puede ser negativo. Intente nuevamente.")
                consumo_turno = float(input(f"Ingrese el consumo en kW: "))
            consumo_diario += consumo_turno