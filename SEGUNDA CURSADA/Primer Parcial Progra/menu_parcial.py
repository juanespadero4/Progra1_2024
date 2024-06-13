from funciones_parcial import *


def imprimir_menu():
    print("MENU PRINCIPAL\n\n1)Registrar proyecto \n2)Modificar proyecto \n3)Cancelar proyecto \n4)Comprobar proyectos \n5)Mostrar todos los proyectos \n6)Calcular presupuesto promedio \n7)Buscar proyecto por nombre \n8)Ordenar proyectos \n9)Retomar proyecto \n10)Salir")

def menu():
    lista_proyectos = abrir()
    while(True):
        imprimir_menu()
        opcion = int(input("Elija una opción: "))
        match opcion:
            case 1:
                incrementar_id(lista_proyectos)
                if menu_agregar_proyecto(lista_proyectos):
                    print("PROYECTO DADO DE ALTA")
                else:
                    decrementar_id()
                    print("ALTA DE PROYECTO CANCELADA")
            case 2:
                mostrar_proyectos(lista_proyectos)
                modificar_proyecto(lista_proyectos)
            case 3:
                baja_proyecto(lista_proyectos)
            case 4:
                comprobar_proyectos_finalizados(lista_proyectos)
            case 5:
                mostrar_proyectos(lista_proyectos)
            case 6:
                presupuesto_promedio(lista_proyectos)
            case 7:
                buscar_proyecto_nombre(lista_proyectos)
            case 8:
                pass
            case 9:
                pass
            case 10:
                print("Saliendo del programa, hasta pronto!")
                # cerrar_csv(lista_proyectos)
                break
        input("Presione enter para continuar...")
menu()