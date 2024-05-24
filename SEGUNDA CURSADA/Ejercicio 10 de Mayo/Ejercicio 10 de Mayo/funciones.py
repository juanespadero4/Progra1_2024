import datetime

def obtener_fecha_actual():
    fecha_hoy = datetime.date.today() #Para obtener la fecha de hoy
    fecha_formato_perzonalizado = fecha_hoy.strftime("%d/%m/%Y") #Para cambiar el formato a dia/mes/año
    
    return fecha_formato_perzonalizado

def nombre_mascota (nombre):
    if nombre != str or nombre == "":
        mensaje = "ERROR, Ingrese el nombre de su mascota nuevamente"
        return mensaje
    else:
        return nombre

def dni_dueño (dni):
    if len(dni) < 7 or len(dni) > 8 or dni != int:
        mensaje = "ERROR, se ingresaron caracteres no numericos o el dni no tiene entre 7 y 8 numeros"
        return mensaje
    else:
        return dni
    
def edad_mascota (edad):
    if edad == 0 or edad != int or edad < 0:
        mensaje = "ERROR, se ingreso una edad invalida."
        return mensaje
    else:
        return edad
    
def especie_mascota (especie):
    if especie != str or especie == "":
        mensaje = "ERROR, la especie de la mascota no puede ser numerica o vacio."
        return mensaje
    else:
        return especie

def sexo_mascota (sexo):
    if sexo == 1:
        sexo = "Macho"
        return sexo
    elif sexo == 2:
        sexo = "Hembra"
        return sexo
    else:
        mensaje = "ERROR, debe seleccionar la opcion 1 o la opcion 2"
        return mensaje
    
def peso_mascota (peso):
    if peso < 0 or peso != float:
        mensaje = "ERROR, el peso debe ser numerico y no puede ser menor que 0"
        return mensaje 
    else:
        return peso
    
def dia (dia):
    if dia != int or dia < 1 or dia > 31:
        mensaje = "ERROR, vuelva a introducir el dia."
        return mensaje
    else:
        return dia
    
def mes (mes):
    if mes != int or mes < 1 or mes > 12:
        mensaje = "ERROR, vuelva a introducir el mes."
        return mensaje
    else:
        return mes

def año (año):
    if año != int or año < 2020:
        mensaje = "ERROR, vuelva a introducir el año."
        return mensaje
    else:
        return año
    
def fecha_completa (dia, mes, año):
    mensaje = f"{dia}/{mes}/{año}"
    return mensaje

def historial_medico (motivo):
    if motivo != str:
        mensaje = "ERROR, se espera el motivo de visita de la mascota"
        return mensaje
    else:
        return motivo