filosofos = ['Marx','Mileto','Platón','Sócrates']

#for filosofo in filosofos:
#    print(filosofo)

#for filosofo in filosofos[1:3]:
#    print (filosofo)

for filosofo in filosofos:
    if filosofo == 'Platón':
        print(f'{filosofo} - es el mejor.')
        break
    else:
        print(filosofo)
