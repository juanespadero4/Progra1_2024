import datetime
id_autoincremental = 0
lista_proyectos = [
    {
        "id": 1,
        "nombre": "Pepe",
        "descripcion": "ARGENTO",
        "fecha_inicio": "2021-02-01",
        "fecha_finalizacion": "2022-04-05",
        "presupuesto": 600000,
        "estado_actual": "Activo"
    },
    {
        "id": 2,
        "nombre": "Luna",
        "descripcion": "Proyecto Lunar",
        "fecha_inicio": "2022-01-15",
        "fecha_finalizacion": "2023-06-30",
        "presupuesto": 750000,
        "estado_actual": "Activo"
    },
    {
        "id": 3,
        "nombre": "Marte",
        "descripcion": "Exploracion Marciana",
        "fecha_inicio": "2021-07-20",
        "fecha_finalizacion": "2022-12-15",
        "presupuesto": 800000,
        "estado_actual": "Activo"
    },
    {
        "id": 4,
        "nombre": "Solar",
        "descripcion": "Energía Solar",
        "fecha_inicio": "2023-03-01",
        "fecha_finalizacion": "2024-05-20",
        "presupuesto": 900000,
        "estado_actual": "Activo"
    }
]


def incrementar_id():
    global id_autoincremental
    id_autoincremental +=1

def decrementar_id():
    global id_autoincremental
    id_autoincremental +=-1

def dividir(divisor, dividendo):
    division = dividendo / divisor
    return division

def obtener_nombre_proyecto(mensaje: str):
    while True:
        nombre_proyecto = input(mensaje)
        nombre_proyecto = nombre_proyecto.capitalize()
        if nombre_proyecto.isalpha() and 0 < len(nombre_proyecto) <= 30:
            return nombre_proyecto
        else:
            print("ERROR, ingrese solo caracteres alfabéticos y asegúrese de que no exceda los 30 caracteres.")

def obtener_descripcion():
    while True:
        descripcion = input("Ingrese la descripcion del proyecto: ")
        descripcion = descripcion.capitalize()
        if len(descripcion) <= 200:
            return descripcion
        else:
            print("ERROR, ha pasado los 200 caracteres.")

def validar_presupuesto():
        while True:
            presupuesto = int(input("Ingrese el presupuesto del proyecto (no menor a 500000): "))
            if presupuesto >= 500000:
                return presupuesto
            else:
                print("ERROR, reingrese un presupuesto valido.")

def es_bisiesto(año):
    """Verifica si un año es bisiesto."""
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

def validar_fecha(dia, mes, año):
    """Valida que la fecha sea correcta."""
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        if es_bisiesto(año) and dia > 29:
            return False
        elif not es_bisiesto(año) and dia > 28:
            return False
    if dia > 31:
        return False
    return True

def solicitar_fecha(inicio_o_final: str):
    """Solicita al usuario que ingrese una fecha válida en formato DD/MM/AAAA."""
    while True:
            dia = int(input(f"Ingrese el día de {inicio_o_final} (DD): "))
            mes = int(input(f"Ingrese el mes de {inicio_o_final} (MM): "))
            año = int(input(f"Ingrese el año de {inicio_o_final} (AAAA): "))

            if validar_fecha(dia, mes, año):
                fecha = datetime.date(año, mes, dia)
                return fecha.strftime("%Y-%m-%d")
            else:
                print("Fecha no válida. Intente nuevamente.")

def solicitar_fecha_final(fecha_inicio):
    while True:
        fecha_final = solicitar_fecha("finalizacion")
        if fecha_final > fecha_inicio:
            return fecha_final
        else:
            print("La fecha de finalizacion es anterior a la de inicio, por favor reintroduzca una fecha valida.")

def estado_proyecto():
    estado = input("Ingrese el estdo del proyecto(Activo/Cancelado/Finalizado): ")
    estado = estado.capitalize()
    if estado == "Activo":
        return estado
    elif estado == "Cancelado":
        return estado
    elif estado == "Finalizado":
        return estado
    else:
        print("Se ingreso un estado de proyecto incorrecto, por favor elija una de las 3 opciones.")

def confirmar_alta():
        while True:
            confirmar_o_cancelar = input("Desea dar de alta el proyecto? (Si/No): ")
            confirmar_o_cancelar.capitalize()
            if confirmar_o_cancelar == "Si":
                return True
            else:
                return False

def mostrar_proyecto(proyecto):
    """Muestra la información de un proyecto en forma de tabla."""
    headers = ["ID", "Nombre del Proyecto", "Descripción", "Fecha de Inicio", "Fecha de Fin", "Presupuesto", "Estado"]
    data = [
        proyecto["id"],
        proyecto["nombre"],
        proyecto["descripcion"],
        proyecto["fecha_inicio"],
        proyecto["fecha_finalizacion"],
        proyecto["presupuesto"],
        proyecto["estado_actual"]
    ]
    print(f"{headers[0]:<5} | {headers[1]:<20} | {headers[2]:<30} | {headers[3]:<12} | {headers[4]:<12} | {headers[5]:<10} | {headers[6]:<12}")
    print("-" * 120)
    print(f"{data[0]:<5} | {data[1]:<20} | {data[2]:<30} | {data[3]:<12} | {data[4]:<12} | {data[5]:<10} | {data[6]:<12}")

def mostrar_proyectos(lista_proyectos):
    """Muestra la información de todos los proyectos en forma de tabla."""
    if not lista_proyectos:
        print("No hay proyectos registrados.")
        return

    headers = ["ID", "Nombre del Proyecto", "Descripción", "Fecha de Inicio", "Fecha de Fin", "Presupuesto", "Estado"]
    print(f"{headers[0]:<5} | {headers[1]:<20} | {headers[2]:<30} | {headers[3]:<12} | {headers[4]:<12} | {headers[5]:<10} | {headers[6]:<12}")
    print("-" * 120)

    for proyecto in lista_proyectos:
        data = [
            proyecto["id"],
            proyecto["nombre"],
            proyecto["descripcion"],
            proyecto["fecha_inicio"],
            proyecto["fecha_finalizacion"],
            proyecto["presupuesto"],
            proyecto["estado_actual"]
        ]
        print(f"{data[0]:<5} | {data[1]:<20} | {data[2]:<30} | {data[3]:<12} | {data[4]:<12} | ${data[5]:<10} | {data[6]:<12}")

def busqueda_proyecto(lista_proyectos: list, id_proyecto: int):
    for id, proyecto in enumerate(lista_proyectos):
        if id_proyecto == proyecto["id"]:
            return id
    return None

def baja_proyecto(lista_proyectos: list):
    if not lista_proyectos:
        print("No hay proyectos para cancelar.")
        return
    mostrar_proyectos(lista_proyectos)
    id_proyecto_a_eliminar = int(input("Ingrese el id del proyecto que desea elimnar de la lista: "))
    proyecto_de_baja = busqueda_proyecto(lista_proyectos, id_proyecto_a_eliminar)
    if proyecto_de_baja != None:
        cancelacion_proyecto = confirmar_alta()
        if cancelacion_proyecto:
            lista_proyectos[proyecto_de_baja]["estado_actual"] = "Cancelado"
            print(f"Proyecto con el {id_proyecto_a_eliminar} ha sido cancelado.")
        else:
            print("Se cancelo la operacion de baja.")
    else:
        print("No se encontro el proyecto.")


def comprobar_proyectos_finalizados(lista_proyectos):
    """Comprueba y actualiza el estado de los proyectos que han finalizado."""
    fecha_actual = datetime.date.today().strftime("%Y-%m-%d")
    for proyecto in lista_proyectos:
        if proyecto["fecha_finalizacion"] <= fecha_actual and proyecto["estado_actual"] == "Activo":
            proyecto["estado_actual"] = "Finalizado"
            print(f"El proyecto con ID {proyecto['id']} ha sido finalizado.")

def presupuesto_promedio(lista):
    """
    Esta función de Python calcula el presupuesto promedio de los proyectos en una lista determinada.
    Retorna el presupuesto promedio de los proyectos en la lista `lista_proyectos`.
    """
    cantidad_proyectos = 0
    suma_presupuestos = 0
    for proyecto in lista:
        cantidad_proyectos += 1
        suma_presupuestos += proyecto["presupuesto"]
    promedio =  dividir(cantidad_proyectos, suma_presupuestos)
    print(f"El promedio de los presupuestos es de ${promedio}.")

def modificar_proyecto(lista_proyectos):
    id_a_modificar = int(input("Ingrese el ID del proyecto a modificar: "))
    for id, proyecto in enumerate(lista_proyectos):
        if id_a_modificar == proyecto["id"]:
            menu_modificaciones = int(input(
                "Seleccione qué opción desea modificar:\n"
                "1) Nombre\n"
                "2) Descripción\n"
                "3) Fecha de inicio\n"
                "4) Fecha de finalizacion\n"
                "5) Presupuesto\n"
                "6) Volver al menu"
                "Opcion a ingresar: "
            ))
            match menu_modificaciones:
                case 1:
                    nuevo_nombre = obtener_nombre_proyecto("Escriba aquí el nuevo nombre del proyecto: ")
                    lista_proyectos[id]["nombre"] = nuevo_nombre
                    print("NOMBRE CAMBIADO CON ÉXITO.")
                case 2:
                    nueva_descripcion = obtener_descripcion()
                    lista_proyectos[id]["descripcion"] = nueva_descripcion
                    print("DESCRIPCIÓN CAMBIADA CON ÉXITO.")
                case 3:
                    nueva_fecha_inicio = solicitar_fecha("inicio")
                    lista_proyectos[id]["fecha_inicio"] = nueva_fecha_inicio
                    print("FECHA DE INICIO CAMBIADA CON ÉXITO.")
                case 4:
                    nueva_fecha_final = solicitar_fecha("finalización")
                    lista_proyectos[id]["fecha_finalizacion"] = nueva_fecha_final
                    print("FECHA DE FINALIZACIÓN CAMBIADA CON ÉXITO.")
                case 5:
                    nuevo_presupuesto = validar_presupuesto()
                    lista_proyectos[id]["presupuesto"] = nuevo_presupuesto
                    print("PRESUPUESTO CAMBIADO CON ÉXITO.")
                case 6:
                    break
    else:
        print("No se encontró el proyecto con el ID especificado.")


def buscar_proyecto_nombre():
    nombre_proyecto_a_buscar = obtener_nombre_proyecto("Ingrese el nombre del proyecto a buscar: ")
    for proyecto in lista_proyectos:
        if nombre_proyecto_a_buscar == proyecto["nombre"]:
            print("Se encontro el proyecto.")
            mostrar_proyecto(proyecto)
    

#-------------------------------------------------------------------------------------------------------------------

def menu_agregar_proyecto():
    global id_autoincremental
    retorno = False
    nombre_proyecto = obtener_nombre_proyecto("Ingrese el nombre del proyecto: ")
    descripcion_proyecto = obtener_descripcion()
    fecha_inicio = solicitar_fecha("inicio")
    fecha_final = (solicitar_fecha_final(fecha_inicio))
    presupuesto_proyecto = validar_presupuesto()
    estado_actual_proyecto = estado_proyecto()
    proyecto = {"id": id_autoincremental, 
                "nombre": nombre_proyecto, 
                "descripcion": descripcion_proyecto, 
                "fecha_inicio": fecha_inicio, 
                "fecha_finalizacion": fecha_final, 
                "presupuesto": presupuesto_proyecto, 
                "estado_actual": estado_actual_proyecto
                }
    mostrar_proyecto(proyecto)
    alta_proyecto = confirmar_alta()
    if alta_proyecto:
        lista_proyectos.append(proyecto)
    return lista_proyectos




