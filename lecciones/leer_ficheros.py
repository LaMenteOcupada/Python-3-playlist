# ipsum_fichero = open('ficheros/ipsum.txt')
# #
# # for linea in ipsum_fichero:
# #     print(linea.rstrip())
# #
# # ipsum_fichero.seek(0)
# #
# # lineas = ipsum_fichero.readlines()
# # print (lineas)
#
# ipsum_fichero.seek(50)
# fichero_texto = ipsum_fichero.read(100)
# print(fichero_texto)
#
# ipsum_fichero.close()

def secuencia_filtro(linea):
    return '>' not in linea

with open('ficheros/secuencia.txt') as sec_fichero:
    lineas = sec_fichero.readlines()
    print(list(filter(secuencia_filtro,lineas)))

#continuamos
