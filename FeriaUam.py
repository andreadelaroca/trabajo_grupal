#Ejercicio 3: Control de ventas en feria universitaria

#Cree un programa que permita llevar un registro de ventas en una feria estudiantil organizada
#por la UAM. La feria se desarrollará durante tres días, con cuatro stands por día. Cada stand
#ofrecerá tres productos distintos. El sistema deberá permitir ingresar el monto de venta por
#producto y mostrar un resumen por stand, por día, y un total general de la feria"

#Se declaran las variables necesarias, para diferenciar los stands, dias y productos
dias = 3
stands_dias = 4
productos_stands = 3

#hacemos listas anidadadas para almacenar los datos de cada stand, dia y producto con su conteo en 0
ventas = [[[0 for _ in range(productos_stands)] for _ in range(stands_dias)] for _ in range(dias)]

#se inicia el proceso de ingreso de datos
for dia in range(dias):
    print(f"\nDia {dia + 1}") # el +1 es para que el dia empiece desde 1 hasta el tercer dia

    for stand in range(stands_dias):
        print(f"\nStand {stand + 1  }") #El mismo caso que el dia, como son 4 stand por dia va diciendo Stand 1, Stand 2, etc

        for producto in range(productos_stands):    
            print(f"\nProducto {producto + 1}")#Aqui el mismo procedimiento de empezar desde el primer producto por stand hasta el tercer producto      

            while True: #se inicia un bucle para que el usuario ingrese el monto de venta
                try: #este comando se usa con el excepto value para cuando el usuario ingrese un valor no valido, el progama le vuelve a tirar el mensaje sin salir 
                    
                    #ahora le pedimos al usuario que ingrese el monto de venta
                    monto = float(input(f"Ingrese el monto de venta para el Producto {producto + 1}: C$ "))

                    #validamos que el monto no sea negativo
                    if monto < 0:
                        raise ValueError("El monto no puede ser negativo.")
                    
                    #si es valido lo guardamos en la estructura de ventas
                    ventas[dia][stand][producto] = monto

                    break #si los datos pedidos fueron ingresados correctamente, nos saca del bucle

                # ponemos un except value por si el usuario ingresa un valor no valido, le vuelva a pedir el monto
                except ValueError as e:

                    print(f"Error: {e}. Intente nuevamente.")
                    #si el usuario ingresa un valor no valido, le vuelve a pedir el monto
            
#Se procede a mostrar el resumen de las ventas de cada stand por dia
print("\n===Resumen de ventas por stand y dias ===")

#se inicializa una variable para acumular el total de la feria
total_general = 0

#Se hace una esrtructura de bucles anidados para recorrer la lista de ventas
for dia in range(dias):
    total_dia = 0 #se inicializa el total del dia en 0
    print(f" {dia + 1}:")

    for stand in range(stands_dias):
        #se suma las ventas de cada stand
        total_stand = sum(ventas[dia][stand])
        print(f"Stand {stand + 1}: C${total_stand:.2f}")
        total_dia += total_stand #se suma el total del stand al total del dia
    print(f"Total del dia {dia + 1}: C${total_dia:.2f}")
    total_general += total_dia 
    
print(f"Total general de la feria: C${total_general:.2f}")