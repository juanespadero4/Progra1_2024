from funciones import *

id_autoincremental = 0

def incrementar_id():
    global id_autoincremental
    id_autoincremental += 1

def decrementar_id():
    global id_autoincremental
    id_autoincremental +=-1