

def suma (primer_operando: int, segundo_operando: int) -> int:
    suma_operandos = primer_operando + segundo_operando
    return suma_operandos

def resta (primer_operando: int, segundo_operando: int):
    resta_operandos = primer_operando - segundo_operando
    return resta_operandos

def division (primer_operando: int, segundo_operando: int):
    if segundo_operando != 0:
        dividir_operandos = primer_operando / segundo_operando
        return dividir_operandos
    else:
        print("No se puede dividir por 0")
    

def multiplicacion (primer_operando: int, segundo_operando: int):
    multiplicar_operandos = primer_operando + segundo_operando
    return multiplicar_operandos


