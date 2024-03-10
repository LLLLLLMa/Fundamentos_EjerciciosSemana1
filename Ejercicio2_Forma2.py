#Entrada:
    #Ingresos del comprador
    #Costo de la casa
#Proceso:
    #Calcular el pie y los pagos mensuales por los ingresos del comprador
#Salida:
    #Pago del comprador por pie y pagos mensuales

def CalcularValores(ingresos, valor_casa):
    if (ingresos >= 80000):
        pie = valor_casa * 0.15
        meses = 10 * 12
        valor_mensual = (valor_casa - pie) / meses
    else:
        pie = valor_casa * 0.3
        meses = 10 * 7
        valor_mensual = (valor_casa - pie) / meses

    return pie, valor_mensual, meses

def main():
    lista_ingresos = []
    lista_valores_casa = []

    while True:
        while True:
            try:
                nuevo_ingreso = int(input("Ingresos del comprador: "))

                if (nuevo_ingreso <= 0):
                    raise IndexError
                lista_ingresos.append(nuevo_ingreso)
                break

            except ValueError:
                print("ERROR: DEBE INGRESAR UN NUMERO.")

            except IndexError:
                print("ERROR: LOS INGRESOS NO PUEDEN SER MENORES O IGUALES A 0.")

        while True:
            try:
                nuevo_valor_casa = int(input("Valor de la casa: "))

                if (nuevo_valor_casa <= 0):
                    raise IndexError
                
                lista_valores_casa.append(nuevo_valor_casa)

                break

            except ValueError:
                print("ERROR: DEBE INGRESAR UN NUMERO.")

            except IndexError:
                print("ERROR: EL VALOR DE LA CASA NO PUEDE SER MENOR O IGUAL A 0.")
        
        seguir = input("¿Desea seguir añadiendo compradores? Cualquier respuesta que no sea 'Si' se considerara como 'No\n")

        if (seguir != 'Si'):
            break

    for i in range(len(lista_ingresos)):
        ingresos = lista_ingresos[i]
        valor_casa = lista_valores_casa[i]
        pie, valor_mensual, meses = CalcularValores(ingresos, valor_casa)
        print(f"El comprador de ingresos ${ingresos} debe pagar ${pie} como pie y debe pagar ${valor_mensual} por mes durante {meses} meses por una casa de valor ${valor_casa}.")

main()