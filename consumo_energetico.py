# Defini las constantes
num_edificios = 4
dias_semana = 7
turnos_dia = 3

for edificio in range(num_edificios):
    print(f"\nedificio {edificio + 1}:") #Inicio del bucle
    for dia in range(dias_semana):
        print(f" dia {dia + 1}:")
        for turno in range(turnos_dia): #definir los 7 dias de la semana
