with open('ficheros/texto.txt','w') as fichero_escritura:
    fichero_escritura.write('Hola Mentes Ocupadas, python es genial!')

#codigo

with open('ficheros/texto.txt','a') as fichero_escritura:
    fichero_escritura.write('\n Me gusta tanto que pienso en python.')

frases = [

    '\nFrase1',
    '\nFrase2',
    '\nFrase3'

]

with open('ficheros/texto.txt','a') as fichero_escritura:
    fichero_escritura.writelines(frases)
