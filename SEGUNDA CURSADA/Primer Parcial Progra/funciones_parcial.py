id_autoincremental = 0
lista_proyectos = []

def incrementar_id():
    global id_autoincremental
    id_autoincremental +=1

def decrementar_id():
    global id_autoincremental
    id_autoincremental +=-1

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
        if len(descripcion) > 200:
            print("ERROR, ha pasado los 200 caracteres.")
            return descripcion
        else:
            return descripcion

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
                return f"{dia:02d}/{mes:02d}/{año:04d}"
            else:
                print("Fecha no válida. Intente nuevamente.")

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

def menu_agregar_proyecto(id_autoincremental: int):
    nombre_proyecto = obtener_nombre_proyecto("Ingrese el nombre del proyecto: ")
    descripcion_proyecto = obtener_descripcion()
    fecha_inicio = solicitar_fecha("inicio")
    fecha_final = solicitar_fecha("final")  #Falta verificar que la fecha no sea posterior
    presupuesto_proyecto = validar_presupuesto()
    estado_actual_proyecto = estado_proyecto()
    proyecto = {"id": id_autoincremental, "nombre": nombre_proyecto, "descripcion": descripcion_proyecto, "fecha inicio": fecha_inicio, "fecha finalizacion": fecha_final, "presupuesto": presupuesto_proyecto, "estado actual": estado_actual_proyecto}

    lista_proyectos.append(proyecto)
    print("PROYECTO DADO DE ALTA")


menu_agregar_proyecto(id_autoincremental)
print(lista_proyectos)