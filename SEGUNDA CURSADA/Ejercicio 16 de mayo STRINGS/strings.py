"""
    1 Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista en mayusculas

    2 Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista con la primer letra en
    mayusculas y el resto en minusculas

    3 Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista en mayusculas que este
    en un indice par

    4 Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista capitalizada que este
    en un indice impar

    5 Crear una funcion que reciba por parámetro la lista de productos,
    Recorra la lista y obtenga las palabras que esten en un indice par
    solamente, aplicarle mayusculas y mostrarlas todas juntas en un
    nuevo string el cual separe esas palabras con un guion '-'. La cadena
    resultante debe estar formateada usando el método format()
    Ejemplo de salida: "MATE-HARINA-YERBA-CACAO-PATE-ARROZ-SARDINAS-CHOCLO"

    6 Crear una funcion que reciba por parámetro la lista de productos,
    la Recorra la lista y obtenga las palabras que esten en un indice impar
    solamente y además:
    A) Si tiene mas de 4 caracteres, aplicarle mayusculas.
        A.1) Si tiene mas de una letra 'A' (mayuscula o minuscula), 
            sumarla a la cantidad de a una variable contador_de_a
            que estara previamente inicializado en 0 al inicio de la funcion
    B) Si tiene hasta 4 caracteres, capitalizarlas.

    al resultado mostrarlas todas juntas en un nuevo string el cual 
    separe esas palabras con un guion '-'. Las cadenas resultantes
    deben estar formateadas con la interpolación de strings o f-strings
    Ejemplo de salida: 
    "Mate,HARINA,YERBA,CACAO,Pate,ARROZ,SARDINAS,CHOCLO"
    "Cantidad de letras A: 6"

    7 Crear una funcion que reciba por parámetro la lista de productos,
    Recorra la lista, las ponga en minusculas y las concatene en un string, 
    separadas por una coma ',' (Desde el primer elemento de la lista hasta 
    el anteultimo inclusive). Finalmente ese string resultante deberas concatenarla al
    ultimo elemento de la lista con una ' y '. Luego de eso, imprimir el 
    string resultante.
    Ejemplo de salida: 
    "mate,cafe,harina,palmitos,yerba,mermelada,cacao,picadillo,pate,caballa,arroz,arvejas,sardinas,atún,choclo y lentejas"
    """

# Desarrollar aca las funciones:
# Ejercicio 1
def recorrer_e_imprimir_en_minusculas(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista en mayusculas
    """
    for producto in productos:
        print(producto.upper())
        print("---------------------------------------")
    print("=======================================")

# Ejercicio 2
def recorrer_e_imprimir_capitalizando(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista con la primer letra en
    mayusculas y el resto en minusculas
    """
    for producto in productos:
        print(producto.capitalize())
        print("---------------------------------------")
    print("=======================================")
    pass

# Ejercicio 3
def recorrer_e_imprimir_mayusculas_indice_par(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista en mayusculas que este
    en un indice par
    """
    for indice, producto in enumerate(productos):
        if indice % 2 == 0:
            print(producto.upper())
            print("---------------------------------------")
    print("=======================================")

# Ejercicio 4
def recorrer_e_imprimir_capitalizada_indice_impar(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista capitalizada que este
    en un indice impar
    """
    for indice, producto in enumerate(productos):
        if indice % 2 != 0:
            print(producto.upper())
            print("---------------------------------------")
    print("=======================================")
    pass

# Ejercicio 5
def recorrer_e_imprimir_mayusculas_indice_par_formateadas(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos,
    Recorra la lista y obtenga las palabras que esten en un indice par
    solamente, aplicarle mayusculas y mostrarlas todas juntas en un
    nuevo string el cual separe esas palabras con un guion '-'. La cadena
    resultante debe estar formateada usando el método format()
    Ejemplo de salida: "MATE-HARINA-YERBA-CACAO-PATE-ARROZ-SARDINAS-CHOCLO"
    """
    posiciones_pares = []
    for indice, producto in enumerate(productos):
        if indice % 2 == 0:   
            posiciones_pares.append(producto.upper())
    cadena = "-".join(posiciones_pares)
    print(cadena)


# Ejercicio 6
def recorrer_e_imprimir_indice_impar_formateadas_y_contabilizar(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos,
    la Recorra la lista y obtenga las palabras que esten en un indice impar
    solamente y además:
        A) Si tiene mas de 4 caracteres, aplicarle mayusculas.
        A.1) Si tiene mas de una letra 'A' (mayuscula o minuscula), 
                sumarla a la cantidad de a una variable contador_de_a
                que estara previamente inicializado en 0 al inicio de la funcion
        B) Si tiene hasta 4 caracteres, capitalizarlas.

        al resultado mostrarlas todas juntas en un nuevo string el cual 
        separe esas palabras con un guion '-'. Las cadenas resultantes
        deben estar formateadas con la interpolación de strings o f-strings
        Ejemplo de salida: 
        "Mate,HARINA,YERBA,CACAO,Pate,ARROZ,SARDINAS,CHOCLO"
        "Cantidad de letras A: 6"
    """
    indice_impar_formateadas = []
    cantidad_de_a = 0
    for indice, producto in enumerate(productos):
        if indice % 2 != 0:
            if len(producto) > 4:
                indice_impar_formateadas.append(producto.upper())
                cantidad_de_a += producto.lower().count('a')
            elif len(producto) <= 4:
                indice_impar_formateadas.append(producto.capitalize())
                cantidad_de_a += producto.lower().count('a')
    final = "-".join(indice_impar_formateadas)
    print(final)
    print(f"Cantidad de letras A: {cantidad_de_a}")

# Ejercicio 7
def recorrer_e_imprimir_elementos_minusculas_formateadas(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos,
    Recorra la lista, las ponga en minusculas y las concatene en un string, 
    separadas por una coma ',' (Desde el primer elemento de la lista hasta 
    el anteultimo inclusive). Finalmente ese string resultante deberas concatenarla al
    ultimo elemento de la lista con una ' y '. Luego de eso, imprimir el 
    string resultante.
    Ejemplo de salida: 
    "mate,cafe,harina,palmitos,yerba,mermelada,cacao,picadillo,pate,caballa,arroz,arvejas,sardinas,atún,choclo y lentejas"
    """
    productos_minusculos = []
    for producto in productos [:-1]:
        productos_minusculos.append(producto.lower())
    cadena = ",".join(productos_minusculos)
    resultado = f"{cadena} y {productos[-1]}"
    print(resultado)
