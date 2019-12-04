num1 = 3.14256789
num2 = 10.1234567

#PREVIAMENTE
#abriendo y cerrando strings, sin opciones de formaro
print('num1 es ',num1,' y num2 es ', num2)

#FORMAT
#el orden es importante,primer numero es el indice, :especifica las opciones de formato
print('num1 es {0:.3f} y  num2 es {1:.3f}'.format(num1,num2))

#USANDO F-STRING
#sin que importe el orden,
print(f'num1 es {num1:.4f} y num2 es {num2:.4f}')

# EJEMPLO DEL SISTEMA DE FICHEROS
folder = 'Sandbox'
print(fr'C:\User\Documents\{folder}')
