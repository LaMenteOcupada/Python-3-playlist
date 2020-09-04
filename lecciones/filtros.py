notas = [ 5 , 4 , 9 , 10 , 4]

def quita_suspensos(nota):
    return nota != 4

# print(list(filter(quita_suspensos,notas)))

# notas_filtradas = []
# for nota in notas:
#     if nota != 4:
#         notas_filtradas.append(nota)
# print(notas_filtradas)

print([nota for nota in notas if nota !=4])
