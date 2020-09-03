from random import shuffle

def mezcla(palabra):
    anagramas = list (palabra)
    shuffle(anagramas)
    return ''.join(anagramas)

palabras = ['docker','synology','python']
anagramas = []

# for palabra in palabras:
#     anagramas.append(mezcla(palabra))
# print(anagramas)
#print(list(map (mezcla,palabras)))

print( [mezcla(palabra)for palabra in palabras] )
