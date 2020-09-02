precios = [3,5,7,10,100]
#doblando precios
doble_precios = []
for precio in precios:
    doble_precios.append(precio*2)
print(doble_precios)

#Método de comprensión(comprehension method)
doble_precios = [precio*2 for precio in precios]
print(doble_precios)

#raiz cuadrada
nums = [1,2,3,4,5,6,7,8]

raizcuadrada_numeros_pares = []
for num in nums:
    if(num ** 2)%2 == 0:
        raizcuadrada_numeros_pares.append(num ** 2)
print(raizcuadrada_numeros_pares)

#Método de comprensión(comprehension method)
raizcuadrada_numeros_pares = [num**2 for num in nums if(num**2) % 2 == 0]
print(raizcuadrada_numeros_pares)
