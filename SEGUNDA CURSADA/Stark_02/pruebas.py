from data_stark import *

def obtener_nombre(diccionario):
    return f"Nombre: {diccionario['nombre']}"

def imprimir_dato(dato):
    print(dato)

def utn_imprimir_nombres_personajes(diccionario):
    if not diccionario:
        print("ERROR, lista vacía")
    else:
        for personaje in diccionario:
            nombre_formateado = obtener_nombre(personaje)
            imprimir_dato(nombre_formateado)

def obtener_nombre_y_dato(diccionario, clave):
    resultados = []
    for personaje in diccionario:
        nombre_formateado = obtener_nombre(personaje)
        valor = personaje.get(clave)  
        nombre_dato = f"{nombre_formateado} | {clave}: {valor}."
        resultados.append(nombre_dato)
    
    return resultados

def utn_imprimir_nombres_alturas(diccionario):
    if not diccionario:
        print("ERROR, lista vacía")
    else:
        resultados = obtener_nombre_y_dato(diccionario, "altura")
        for resultado in resultados:
            imprimir_dato(resultado)

utn_imprimir_nombres_alturas(lista_personajes[1])

