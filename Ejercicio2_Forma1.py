#Entrada:
    #Ingresos del comprador
    #Costo de la casa
#Proceso:
    #Calcular el pie y los pagos mensuales por los ingresos del comprador
#Salida:
    #Pago del comprador por pie y pagos mensuales

def main():
    while True:
        try:
            ingresos = int(input("Ingresos del comprador: "))

            if (ingresos <= 0):
                raise IndexError
            break

        except ValueError:
            print("ERROR: DEBE INGRESAR UN NUMERO.")

        except IndexError:
            print("ERROR: LOS INGRESOS NO PUEDEN SER MENORES O IGUALES A 0.")

    while True:
        try:
            valor_casa = int(input("Valor de la casa: "))

            if (valor_casa <= 0):
                raise IndexError
            break

        except ValueError:
            print("ERROR: DEBE INGRESAR UN NUMERO.")

        except IndexError:
            print("ERROR: EL VALOR DE LA CASA NO PUEDE SER MENOR O IGUAL A 0.")

    if (ingresos >= 80000):
        pie = valor_casa * 0.15
        meses = 10 * 12
        valor_mensual = (valor_casa - pie) / meses
    else:
        pie = valor_casa * 0.3
        meses = 10 * 7
        valor_mensual = (valor_casa - pie) / meses

    print(f"El comprador de ingresos ${ingresos} debe pagar ${pie} como pie y debe pagar {valor_mensual} por mes durante {meses} meses por una casa de valor {valor_casa}")

main()