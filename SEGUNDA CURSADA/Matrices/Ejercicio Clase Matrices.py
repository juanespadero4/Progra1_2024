lista_alumnos = []

def incluir_datos():
    for i in range(1):
        bloque_alumno = []
        for dato in range(1):
            nombre = input("Nombre del alumno:")
            nombre_validado = solo_str(nombre)
            edad = input("Edad del alumno:")
            edad_validada = solo_numeros_enteros(edad)
            dni = input("DNI del alumno:")
            dni_validado = solo_numeros_enteros(dni)
            genero = input("Genero del alumno (M, F o NB en mayuscula) :")
            genero_validado = validacion_genero(genero)
            nota = input("Nota del alumno:")
            nota_validada = solo_numeros_enteros_flotantes(nota)
            bloque_alumno.append(nombre, edad_validada, dni_validado, genero, nota_validada)
        lista_alumnos.append(bloque_alumno)


def solo_numeros_enteros (variable):
    if variable != int:
        mensaje = print("ERROR! La opcion elegida debe contener solo contenido numerico y esta contiene otros caracteres, vuelva a intentarlo")
        return mensaje
    else:
        return variable

def solo_numeros_enteros_flotantes (variable) :
    if variable != int or variable != float:
        mensaje = print("ERROR! La opcion elegida debe contener solo contenido numerico y esta contiene otros caracteres, vuelva a intentarlo")
        return mensaje
    else:
        return variable
    
def solo_str (variable):
    if variable != str:
        mensaje = print("ERROR! La opcion elegida debe contener solo letras y esta contiene otros caracteres, vuelva a intentarlo")
        return mensaje
    else:
        return variable

def validacion_genero (variable):
    if variable != "M" or variable != "F" or variable != "NB":
        mensaje = print("ERROR! El genero debe ser M, F o NB y esta contiene otros caracteres, vuelva a intentarlo")
        return mensaje
    else:
        return variable






