from strings import *

if __name__ == '__main__':
    productos = [
        "mate", "caFe", "harina",
        "pAlmitos", "yerBA", "merMElada",
        "cacao", "picadillo", "pate", 
        "CABALLA", "arroz", "ArbEJaS",
        "Sardinas","atún","Choclo","lentejas"
    ]
    # Llamada de cada una de las funciones desarrolladas
    recorrer_e_imprimir_en_minusculas(productos)
    recorrer_e_imprimir_capitalizando(productos)
    recorrer_e_imprimir_mayusculas_indice_par(productos)
    recorrer_e_imprimir_capitalizada_indice_impar(productos)
    recorrer_e_imprimir_mayusculas_indice_par_formateadas(productos)
    recorrer_e_imprimir_indice_impar_formateadas_y_contabilizar(productos)
    recorrer_e_imprimir_elementos_minusculas_formateadas(productos)