# MIT License
#
# Copyright (c) 2024 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# llamar aca cada una de las funciones con prefijo 'utn_' para usarlas en el cuerpo del match
from utn_biblioteca import *
from data_stark import lista_personajes

def utn_personajes_app(diccionario: list[dict]) -> None:
    while  True:
        match utn_menu_principal():
            case 1:
                utn_imprimir_nombres_personajes(diccionario)
            case 2:
                utn_imprimir_nombres_alturas(diccionario)
            case 3:
                utn_calcular_imprimir_heroe(diccionario, "maximo", "altura")
            case 4:
                utn_calcular_imprimir_heroe(diccionario, "minimo", "altura")
            case 5:
                utn_calcular_imprimir_promedio_dato (diccionario, "altura")
            case 6:
                imprimir_dato(identificar_personaje_mas_o_menos (diccionario, "maximo", "altura"))
                imprimir_dato(identificar_personaje_mas_o_menos (diccionario, "minimo", "altura"))
            case 7:
                utn_calcular_imprimir_heroe(diccionario , "maximo", "peso")
                utn_calcular_imprimir_heroe(diccionario, "minimo", "peso")
            case 8:
                utn_calcular_imprimir_heroe(diccionario , "maximo", "poder")
                utn_calcular_imprimir_heroe(diccionario, "minimo", "poder")
            case 9:
                utn_calcular_imprimir_promedio_dato(diccionario, "poder")
                mensaje = "-Los siguientes personajes estan por debajo del promedio:"
                imprimir_dato(mensaje)
                calcular_personajes_por_debajo_del_promedio(diccionario,"poder")
            case 10:
                mensaje = f"El largo de la lista es de {len(diccionario)} personajes."
                imprimir_dato(mensaje)
            case 11:
                contar_personajes_por_franquicia(diccionario, "DC Comics", "Marvel Comics")
            case 12:
                ordenar_personajes_descendente(lista_personajes, "poder")
            case 13:
                ordenar_personajes_ascendente(lista_personajes, "inteligencia")
            case 14:
                calcular_promedio_dato_genero(lista_personajes, "F", "poder")
            case 15:
                calcular_promedio_dato_genero(lista_personajes, "M", "poder")
            case 16:
                break
        limpiar_consola()