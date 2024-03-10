#Datos de entrada: 
    #Edad, Precio del asiento,
#Proceso: 
    #Calcular el descuento por la edad del precio del asiento.
    #La edad no puede ser menor que 5
#Salida: 
    #Perdida por descuento

def CalcularPerdida(edad, precio):
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

    return (precio*descuento)

def main():
    edades = []
    perdidas = []

    while True:
        try:
            nueva_edad = int(input("Ingrese la edad del cliente: "))

            if (nueva_edad < 5):
                raise IndexError
            
            edades.append(nueva_edad)

            seguir = input("¿Desea continuar añadiendo edades para comprobar su perdida?\n(Cualquier otra respuesta que no sea 'Si' sera considerada como 'No'): ")
            
            if (seguir != "Si"):
                break;

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

    for edad in edades:
        perdidas.append(CalcularPerdida(edad, precio))

    for i in range(len(perdidas)):
        print(f"Se pierde ${perdidas[i]} por un cliente de edad {edades[i]}")


main()