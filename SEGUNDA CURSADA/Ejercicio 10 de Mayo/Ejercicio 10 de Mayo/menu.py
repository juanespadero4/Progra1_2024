from funciones import *
from os import *

registro_mascotas = [
    [1,"12345678", "Luna", 3, "Perro", "Hembra", 8.5, "01/05/2024", "Vacunación anual"],
    [2,"23456789", "Max", 7, "Gato", "Macho", 5.2, "28/04/2024", "Control de pulgas"],
    [3,"34567890", "Kiwi", 1, "Dragón", "Hembra", 88000, "02/05/2024", "Recorte de alas"],
    [4,"45678901", "Rocky", 5, "Perro", "Macho", 12.1, "30/04/2024", "Revisión dental"],
    [5,"56789012", "Coco", 2, "Gato", "Hembra", 4.8, "03/05/2024", "Desparasitación"]
]


id_auto_incremental = registro_mascotas[len(registro_mascotas)-1][0] #Obtengo el último id

def incrementar_id():
    global id_auto_incremental
    id_auto_incremental +=1
    
def imprimir_menu():
    #NO TOCAR
    system('clear') #Linux/Mac
    #system('cls') #Windows
    print("MENU PRINCIPAL\n\n1)Registrar Mascota \n2)Actualizar informacion mascota \n3)Mostrar mascotas \n4)Mostrar informacion de las mascotas que solo superen el promedio de edad \n5)Calcular el promedio de peso de todas las mascotas \n6)Ordenar mascotas por edad descendente \n7)Ordenar mascotas en orden alfabetico \n8)Salir del programa")


def menu():
    while(True):
        imprimir_menu()
        opcion = int(input("Elija una opción: "))
        #NO TOCAR
        system('clear') #Linux/Mac
        #system('cls') #Windows
        match opcion:
            case 1:
                incrementar_id()
                dni_dueño_mascota = input ("Ingrese el dni del dueño de la mascota:")
                dni_validado = dni_dueño(dni_dueño_mascota)
                nombre_mascota_nueva = input("Ingrese el nombre de su mascota:")
                nombre_validado = nombre_mascota(nombre_mascota_nueva)
                edad_mascota_nueva = input ("Ingrese la edad de su mascota:")
                edad_validada = edad_mascota(edad_mascota_nueva)
                especie_mascota_nueva = input ("ingrese la especie a la que pertenece su mascota:")
                especie_validada = especie_mascota(especie_mascota_nueva)
                sexo_mascota_nueva = input ("Ingrese el sexo de su mascota. 1 para MACHO o 2 para HEMBRA:")
                sexo_validado = sexo_mascota(sexo_mascota_nueva)
                peso_mascota_nueva =  input ("Ingrese el peso de su mascota:")
                peso_validado = peso_mascota(peso_mascota_nueva)
                dia_visita = input("Ingrese el dia de su visita:")
                mes_visita = input("Ingrese el mes de su visita:")
                año_visita = input("Ingrese el año de su visita:")
                fecha_validada = fecha_completa (dia(dia_visita), mes(mes_visita), año(año_visita))
                historial_medico_mascota = input ("Ingrese el motivo de visita:")
                historial_validado = historial_medico(historial_medico_mascota)
                registro_mascotas.append(dni_validado, nombre_validado, edad_validada, especie_validada, sexo_validado, peso_validado, fecha_validada, historial_validado)
            case 2:
                print("Actualizar informacion en nueva consulta medica.")
            case 3:
                print("Mostrar todas las mascotas.")
            case 4:
                print("Mostrar solo mascotas que superen promedio de edad.")
            case 5:
                print("Calcular el promedio de peso de las mascotas")
            case 6:
                print("Ordenar mascotas por edad (mayor a menor)")
            case 7:
                print("Ordenar mascotas alfabeticamente")
            case 8:
                print("Saliendo del sistema.")
                break
        input("Presione enter para continuar...")
menu()