
def obtener_nombre_o_apellido(mensaje: str):
    while True:
        nombre_o_apellido = input(mensaje)
        nombre_o_apellido = nombre_o_apellido.capitalize()
        if nombre_o_apellido.isalpha() and 0 < len(nombre_o_apellido) <= 20:
            return nombre_o_apellido
        else:
            print("ERROR, ingrese solo caracteres alfabéticos y asegúrese de que no exceda los 20 caracteres.")

def obtener_puesto():
    while True:
        puesto = input("Ingrese el puesto ('Gerente'”' / 'Supervisor'”' / 'Analista'”' / 'Encargado' /  'Asistente'): ")
        puesto = puesto.capitalize()
        if puesto == "Gerente" or puesto != "Supervisor" or puesto != "Analista" or puesto != "Encargado" or puesto != "Asistente":
            return puesto
        else:
            print("ERROR, ingrese algunos de los puestos que le brindamos.")

def validar_dni():
        while True:
            dni = int(input("Ingrese el dni del empleado (entre 5000000 y 99999999): "))
            if dni >= 5000000 and dni <= 99999999:
                return dni
            else:
                print("ERROR, reingrese un dni valido.")

def validar_sueldo():
    while True:
        sueldo = int(input("Ingrese el sueldo de el empleado (no menor a $234315): "))
        if sueldo >= 234315:
            return sueldo
        else:
            print("ERROR, reingrese un sueldo valido.")


def agregar_empleado():
    obtener_nombre_o_apellido("Ingrese el nombre del empleado: ")
    obtener_nombre_o_apellido("Ingrese el apellido del empleado: ")
    validar_dni()
    obtener_puesto()
    validar_sueldo()

agregar_empleado()