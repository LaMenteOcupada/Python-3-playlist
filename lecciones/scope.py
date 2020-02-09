#Scope of a variable /Ambito o alcande de una variable - area o zona donde se puede acceder a una variable

mi_nombre = 'Luis'

def imprime_nombre():
    global mi_nombre
    mi_nombre = 'Marta'
    print('El nombre dentro de la función es ',mi_nombre)

imprime_nombre()

print('El nombre fuera de la función es ',mi_nombre)
