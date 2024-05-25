from data_stark import *
import re
import os

def limpiar_consola():
    _ = input('\nPresione Enter para continuar...')
    if os in ['nt', 'dos', 'ce']:
        os.system('clear')
    else: os.system('cls')

heroe = {}

'''1.1 Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera: 
Nombre: Rambo
'''
def obtener_nombre(diccionario: dict) -> str:
    #Se encarga de extraer el nombre de un personaje del diccionario, se le pasa por parametros un diccionario.
    nombre_heroe = diccionario["nombre"]
    return f"Nombre: {nombre_heroe}"

'''1.2 Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y deberá imprimirlo en la consola. La función no tendrá retorno.'''
def imprimir_dato(dato: str) -> str:
    #imprime lo que se le pase por parametro. El parametro dato puede ser un string, un entero, etc.
    print(dato)

'''1.3 Crear la función 'utn_imprimir_nombres_personajes' la cual recibirá por parámetro la lista de personajes y deberá imprimirla en la consola. Reutilizar las funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.'''
def utn_imprimir_nombres_personajes(diccionario:dict) -> str:
    #La funcion verifica si la lista esta vacia, si esta vacia imprime un mensaje, pero si contiene algo imprime los nombres de los personajes que esten dentro del diccionario pasado por parametro.
    if not diccionario:
        print("ERROR, lista vacía")
    else:
        for personaje in diccionario:
            nombre_formateado = obtener_nombre(personaje)
            imprimir_dato(nombre_formateado)

'''2 Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un personaje y una key (string) la cual representará el dato que se desea obtener. 
-La función deberá devolver un string el cual contenga el nombre y dato (key) del personaje a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.
-El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza). Ejemplo:
Nombre: Venom | fuerza: 500'''

def obtener_nombre_y_dato(heroe: dict, clave: str) -> str:
    #Obtiene el nombre llamando a la funcion nombre_formateado y luego se fija si la clave a buscar esta dentro del diccionario del personaje. Si la clave está, retorna el nombre y el dato en una forma especifica. Se le pasa como parametro el diccionario y la clave a buscar.
    nombre_formateado = heroe["nombre"]
    if clave in heroe:
        dato = heroe[clave]
        return f"{nombre_formateado} | {clave.capitalize()}: {dato}"
    else:
        return f"{nombre_formateado} | {clave.capitalize()}: No disponible"
    

'''3 Crear la función 'utn_imprimir_nombres_alturas' la cual recibirá por parámetro la lista de personajes, la cual deberá iterar e imprimir sus nombres y alturas USANDO la función creada en el punto 2. Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
[Usar esta función en el menú y probar su funcionamiento. Para cual/es opción/es del menú la usarias?]
'''

def utn_imprimir_nombres_alturas(diccionario: dict) -> str:
    #Chequea si el diccionario esta vacio, si es asi retorna -1. De lo contrario recorre e imprime toda la lista con el ombre del personaje y su altura. Se pasa solo el diccionario por parametro.
    if not diccionario:
        return -1
    else:
        for heroe in diccionario:
            resultado = obtener_nombre_y_dato(heroe, "altura")
            imprimir_dato(resultado)

'''4.1 Crear la función 'calcular_max' la cual recibirá por parámetro la lista de personajes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el personaje que tenga el dato más alto.
Ejemplo de llamada:
	calcular_max(lista, 'poder') -> Retorna: El diccionario del personaje q cumpla'''

def calcular_max(diccionario: list, clave: str) -> dict:
    #La función calcular_max calcula el valor máximo de una clave dada en una lista de diccionarios.
    min_value = float('-inf')
    maximo_heroe = None
    for personaje in diccionario:
        if clave in personaje:
            dato = float(personaje[clave])
            if dato > min_value:
                min_value = dato
                maximo_heroe = personaje
    return maximo_heroe


'''4.2 Crear la función 'calcular_min' la cual recibirá por parámetro la lista de personajes y una key (string) la cual representará el dato que deberá ser evaluado a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función deberá poder calcular: el peso, la altura o fuerza máximas y retornar el personaje que tenga el dato más bajo. 
Ejemplo de llamada:
	calcular_min(lista, 'poder') -> Retorna: El diccionario del personaje q cumpla
'''

def calcular_min (diccionario: dict, clave: str) -> dict:
    #La función clacular_min calcula el valor minimo de una clave dada en una lista de diccionarios.
    min_value = float(1000)
    minimo_heroe = None
    for personaje in diccionario:
        if clave in personaje:
            dato = float(personaje[clave])
            if dato < min_value:
                min_value = dato
                minimo_heroe = personaje
    return minimo_heroe

'''4.3 Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:
La lista de personajes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘inteligencia’, etc.
La función deberá retornar el personaje que cumpla con la condición pedida. Reutilizar las funciones hechas en los puntos 4.1 y 4.2
Ejemplo de llamada:
calcular_max_min_dato(lista, "maximo", "poder") -> Retorna: El diccionario del personaje q cumpla
'''
def calcular_max_min_dato(diccionario: dict, maximo_o_minimo: str, clave: str) -> dict:
    #Clacula el maximo  el minimo de la clave que se le pase por parametro. Se le pasa por parametros un diccionario, maximo_o_minimo que recibe "maximo" o "minimo" y la clave a buscar.
    if maximo_o_minimo == "maximo":
        personaje = calcular_max(diccionario, clave)
        return personaje
    elif maximo_o_minimo == "minimo":
        personaje = calcular_min(diccionario, clave)
        return personaje
    else:
        return -1


'''4.4 Crear la función 'utn_calcular_imprimir_heroe' la cual recibirá tres parámetros: 
La lista de personajes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘poder’, etc.

La función deberá obtener el personaje que cumpla dichas condiciones, imprimir su nombre y el valor calculado. Reutilizar las funciones de los puntos:
punto 1.2, punto: 2 y punto 4.3 
Validar que la lista de personajes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
Ejemplo de llamada:
utn_calcular_imprimir_personaje (lista, "maximo", "poder")
Ejemplo de salida:
Mayor poder: Nombre: Godzilla | altura: 119000
[Usar esta función en el menú y probar su funcionamiento. Para cual/es opción/es del menú la usarias?]
'''
def utn_calcular_imprimir_heroe (diccionario: dict, maximo_o_minimo: str, clave: str) -> str:
    #Se chequea que e diccionario no este vacio y si es asi se retorna -1. Caso contrario hara el calculo que se le pida para la cave que se le pida e imprimira al personaje y su dato. Se le pasa por parametros un diccionario, maximo_o_minimo que recibe "maximo" o "minimo" y la clave a buscar.
    if not diccionario:
        return -1
    else:
        heroe_calculado = calcular_max_min_dato(diccionario, maximo_o_minimo, clave)
        imprimir_dato(obtener_nombre_y_dato(heroe_calculado, clave))

'''5.1 Crear la función 'sumar_dato_personaje' la cual recibirá como parámetro una lista de personajes y un string que representara el dato/key de los personajes que se requiere sumar. Validar que cada personaje sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. La función deberá retorna la suma de todos los datos según la key pasada por parámetro
'''

def sumar_dato_personaje(diccionario: dict, clave: str) -> float:
    #Hace una suma de el dato que contenga la clave que se le de. recorre la lista y va sumando los datos. Se le pasa por parametro un diccionario y la clave a calcular.
    suma_dato = 0
    for personaje in diccionario:
        if type(personaje) is dict and personaje:
            suma_dato += personaje.get(clave)
    return suma_dato

'''5.2 Crear la función  ‘dividir’ la cual recibirá como parámetro dos números (dividendo y divisor). Se debe verificar si el divisor es 0,  en caso de serlo, retornar 0 (es matematicamente incorrecto, pero así lo pidió el cliente 🤣), caso contrario realizar la división entre los parámetros y retornar el resultado'''

def dividir(dividendo: int, divisor: int) -> int:
    #Hace una division entre los numero que se le pase por parametero. Recibe dividendo (numero a dividir), y un divisor (numero que divide).
    if divisor == 0:
        return 0
    else:
        division = dividendo / divisor
        division_redondeada = round(division, 2)
        return division_redondeada
    
'''5.3 Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de personajes y un string que representa el dato del personaje que se requiere calcular el promedio (ej: promedio de fuerza, altura, peso, etc). La función debe retornar el promedio (de entre todos los personajes) del dato pasado por parámetro'''

def calcular_promedio (diccionario: dict, clave_a_promediar: str) -> int:
    #Calcula el promedio entre la cantidad de personajes que hay en el diccionario y la suma de la clave pasada. Se pasa por parametro un diccionario, y tambien una clave a promediar. Retorna el promedio calculado.
    cantidad_personajes = len(diccionario)
    total_suma = sumar_dato_personaje(diccionario, clave_a_promediar)
    promedio = dividir (total_suma, cantidad_personajes)
    return promedio

'''5.4 Crear la función 'utn_calcular_imprimir_promedio_dato' la cual recibirá una lista de personajes y un string que representara el dato/clave a calcular, utilizando la función del punto 5.3 calcula y mostrará la altura promedio. Validar que la lista de personajes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.
IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y 5.3
[Usar esta función en el menú y probar su funcionamiento. Para cual/es opción/es del menú la usarias?]
'''
def utn_calcular_imprimir_promedio_dato (diccionario: dict, clave: str) -> str:
    #Imprime el promedio de los datos pasados por parametros. Se le pasa un diccionario y una clave a promediar.
    if diccionario:
        promedio = calcular_promedio (diccionario, clave)
        mensaje = f"-El promedio del {clave.capitalize()} es: {promedio}"
        imprimir_dato(mensaje)
    else:
        return -1

'''6.1 Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, el cual permite utilizar toda la funcionalidad ya programada. Se deberá reutilizar la función antes creada encargada de imprimir un string (1.2)
'''
def imprimir_menu() -> str:
    #Imprime el menu con sus respectivas opciones.
    mensaje = (
        "BIENVENIDO A INDUSTRIAS STARK \n"
        "1) Recorrer la lista imprimiendo por consola el nombre de cada personaje \n"
        "2) Recorrer la lista imprimiendo por consola nombre de cada personaje junto a la altura del mismo. \n"
        "3) Recorrer la lista y determinar cuál es el personaje más alto (MÁXIMO). \n"
        "4) Recorrer la lista y determinar cuál es el personaje más bajo (MÍNIMO). \n"
        "5) Recorrer la lista y determinar la altura promedio de los personajes (PROMEDIO). \n"
        "6) Informar cual es la identidad del personaje asociado a cada uno de los indicadores anteriores (Opción 3 y 4). \n"
        "7) Calcular e informar cual es el personaje más y menos pesado. \n"
        "8) Calcular e informar cual es el personaje más y menos poderoso. \n"
        "9) Determinar el promedio de nivel de poder de todos los personajes e informar qué personaje/s están por debajo de ese poder. \n"
        "10) Calcular e informar la cantidad total de personajes. \n"
        "11) Calcular e informar cuántos personajes son de 'DC Comics' y cuántos de 'Marvel Comics'. \n"
        "12) Ordenar los personajes en orden descendente del que tiene mayor poder al que tiene menos, luego mostrarlos por consola con su nombre y poder. \n"
        "13) Ordenar los personajes en orden ascendente del que tiene menos inteligencia al que tiene más inteligencia. Luego mostrarlos por consola su nombre e inteligencia. \n"
        "14) Calcular e informar el promedio de poder de personajes femeninos. \n"
        "15) Calcular e informar el promedio de poder de personajes masculinos. \n"
        "16) SALIR \n"
    )
    imprimir_dato(mensaje)
    
'''6.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de número el cual deberá verificar que sea sea un string conformado únicamente por dígitos. Retornara True en caso de serlo, False caso contrario
'''
def validar_entero(numero_en_str: str):
    #Valida que el numero en string pasado sea solo digito. Se le pasa por parametro el numero en forma de string.
    return numero_en_str.isdigit()

'''6.3 Crear la función 'utn_menu_principal' la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las funciones del ejercicio 6.1 y 6.2'''

def utn_menu_principal() -> int:  
    #La funcion debe imprimir el menu y da la opcion de ingresar un numero que sera la opcion elegida del menu. Si el numero ingresado contiene letras o no es uno de los numeros de las opciones retornara -1.
    imprimir_menu() 
    opcion_elegida = input("Ingrese la opcion que desea visualizar: ")
    if validar_entero(opcion_elegida):
        return int(opcion_elegida)
    else:
        return -1
    

def identificar_personaje_mas_o_menos(diccionario: dict, max_o_min: str, atributo: str) -> str:
    # Esta función devuelve un mensaje que indica la identidad del personaje con el valor más alto o más bajo para un atributo dado
    personaje = calcular_max_min_dato(diccionario, max_o_min, atributo)
    if max_o_min == "maximo":
        mensaje = f"La identidad del personaje más alto es {personaje["identidad"]} y su altura es {personaje.get(atributo)}"
        return mensaje
    elif max_o_min == "minimo":
        mensaje = f"La identidad del personaje más bajo es {personaje["identidad"]} y su altura es {personaje.get(atributo)}"
        return mensaje


def calcular_personajes_por_debajo_del_promedio(diccionario: dict, atributo: str) -> str:
    # Esta función calcula los personajes por debajo del valor promedio para un atributo dado e imprime sus nombres y valores
    personajes_por_debajo_del_promedio = {}
    promedio = calcular_promedio(lista_personajes, atributo)
    for personaje in diccionario:
        if personaje.get(atributo) < promedio:
            personajes_por_debajo_del_promedio.update(personaje)
            print(obtener_nombre_y_dato(personajes_por_debajo_del_promedio, atributo))


def contar_personajes_por_franquicia(diccionario: dict, franquicia1: str, franquicia2: str) -> str:
    # Esta función cuenta el número de personajes de cada franquicia
    franquicia1_cantidad = 0
    franquicia2_cantidad = 0
    for personaje in diccionario:
        if personaje["empresa"] == franquicia1:
            franquicia1_cantidad += 1
        elif personaje["empresa"] == franquicia2:
            franquicia2_cantidad += 1
    mensaje = f"La cantidad de personajes de {franquicia1} es {franquicia1_cantidad}, y la cantidad de personajes de {franquicia2} es {franquicia2_cantidad}."
    print(mensaje)


def calcular_promedio_dato_genero(diccionario: dict, genero: str, atributo: str) -> float:
    # Esta función calcula el valor promedio de un atributo específico para personajes de un género dado
    personajes_genero = []
    suma_datos = 0
    for personaje in diccionario:
        if personaje.get("genero") == genero:
            personajes_genero.append(personaje)
    promedio = calcular_promedio(personajes_genero, atributo)
    texto = f"El promedio de {atributo.capitalize()} de personajes de género {genero} es: {promedio}"
    print(texto)

def quick_sort_para_claves(diccionario: dict, clave: str):
    # Esta función implementa el algoritmo Quick Sort para ordenar personajes por un atributo específico en orden descendente
    if len(diccionario) <= 1:
        return diccionario
    else:
        pivote = diccionario[0][clave]
        menores = [x for x in diccionario[1:] if x[clave] <= pivote]
        mayores = [x for x in diccionario[1:] if x[clave] > pivote]
        return quick_sort_para_claves(menores, clave) + [diccionario[0]] + quick_sort_para_claves(mayores, clave)


def ordenar_personajes_descendente(diccionario: dict, clave: str):
    # Esta función ordena personajes en orden descendente basándose en un atributo específico
    lista_personajes_ordenada = quick_sort_para_claves(diccionario.copy(), clave)
    for personaje in lista_personajes_ordenada:
        mensaje = obtener_nombre_y_dato(personaje, clave)
        print(mensaje)


def ordenar_personajes_ascendente(diccionario: dict, clave: str):
    # Esta función ordena personajes en orden ascendente basándose en un atributo específico
    lista_personajes_ordenada = quick_sort_para_claves(diccionario.copy(), clave)
    for personaje in lista_personajes_ordenada:
        mensaje = obtener_nombre_y_dato(personaje, clave)
        print(mensaje)
    
    



