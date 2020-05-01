#lección 14
# def mentes_intro(diccionario):
#     for key,val in diccionario.items():
#         print(f'Soy {key} y me interesa {val}')

#Lección 15
def cuenta_intereses(dictionary):
    intereses = list(dictionary.values())
    for interes in set(intereses):
        num = intereses.count(interes)
        print(f'Hay {num} {interes} intereses')

mentes_ocupadas = {}

while True:
    mentes_nombre = input('Introduce el nombre: ')
    mentes_interes = input('Introduce el interes: ')
    mentes_ocupadas[mentes_nombre] = mentes_interes

    otro = input('Añadir otro?(s/n)')
    if otro == 's':
        continue
    else:
        break

#mentes_intro(mentes_ocupadas)
cuenta_intereses(mentes_ocupadas)
