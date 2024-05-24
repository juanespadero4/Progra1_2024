from funciones import *


def menu():

    primer_operando = None
    segundo_operando = None

    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))

        if opcion == 1:
            primer_operando = int(input("Ingrese Primer Operando:"))
        elif opcion == 2:
            segundo_operando = int(input("Ingrese Segundo Operando: "))
        elif opcion == 3:
            if primer_operando == None or segundo_operando == None:
                print("ERROR - No se ha dado un valor numerico a las variables de operando")
            else:
                print("Calculo todas las operaciones")
                suma(primer_operando, segundo_operando)
                resta(primer_operando, segundo_operando)
                division(primer_operando, segundo_operando)
                multiplicacion(primer_operando, segundo_operando)
        elif opcion == 4:
            print("Informo todos los resultados")
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")

            
menu()

