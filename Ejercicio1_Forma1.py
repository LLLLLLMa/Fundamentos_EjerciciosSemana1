#Datos de entrada: 
    #Edad, Precio del asiento,
#Proceso: 
    #Calcular el descuento por la edad del precio del asiento.
    #La edad no puede ser menor que 5
#Salida: 
    #Perdida por descuento

def main():

    while True:
        try:
            edad = int(input("Ingrese la edad del cliente: "))

            if (edad < 5):
                raise IndexError
            break

        except ValueError:
            print("ERROR: INGRESE UN NUMERO COMO EDAD.")

        except IndexError:
            print("ERROR: LOS NIÑOS MENORES DE 5 AÑOS NO PUEDEN ENTRAR.")
    
    while True:
        try:
            precio = float(input("Ingrese el precio unico del asiento: "))
            if (precio <= 0):
                raise IndexError
            break
        
        except ValueError:
            print("ERROR: INGRESE UN NUMERO COMO PRECIO.")

        except IndexError:
            print("ERROR: EL PRECIO NO PUEDE SER MENOR O IGUAL QUE 0")

    if (edad >= 5 and edad <= 14):
        descuento = 0.35
    
    elif (edad >= 15 and edad <= 19):
        descuento = 0.25

    elif (edad >= 20 and edad <= 45):
        descuento = 0.10

    elif (edad >= 46 and edad <= 65):
        descuento = 0.25

    else:
        descuento = 0.35

    perdida = (precio*descuento)

    print(f"Se pierde ${perdida} por un cliente de edad {edad}")

main()