#BUCLES FOR
# filosofos = ['Marx','Mileto','Platón','Sócrates']
#
# #for filosofo in filosofos:
# #    print(filosofo)
#
# #for filosofo in filosofos[1:3]:
# #    print (filosofo)
#
# for filosofo in filosofos:
#     if filosofo == 'Platón':
#         print(f'{filosofo} - es el mejor.')
#         break
#     else:
#         print(filosofo)

#BUCLES WHILE
edad = 30
num = 0

while num < edad:
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print (num)
    if num > 10:
        break
    num += 1
