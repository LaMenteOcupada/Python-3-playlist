from random import randint

palabras_mente = [

    'Intelecto', 'comprensión','razón', 'juicio', 'perspicacia',
    'astucia', 'talento', 'mente', 'capacidad', 'materia gris',
    'cerebro', 'entendimiento', 'raciocinio', 'percepción',
    'conocimiento', 'consciente','subconsciente', 'ingenio',
    'genio', 'genialidad', 'lucidez', 'mentalidad', 'agudeza',
    'discernimiento', 'pensamiento', 'reflexión'

]

def menterizar(palabra):
    random_pos = randint(0, len(palabras_mente) - 1)
    return f'{palabra} {palabras_mente[random_pos]}'

parrafos = int(input('Cuantos parrafos de mentes ipsum:'))

with open('ipsum.txt') as ipsum_original:
    objetos = ipsum_original.read().split()

    for n in range(parrafos):
        mentes_text = list(map(menterizar , objetos))
        with open('mente_ipsum.txt','a')as ipsum_mente:
            ipsum_mente.write('  '.join(mentes_text) + '\n\n')
