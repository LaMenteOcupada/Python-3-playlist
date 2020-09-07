# decorators en inglés
def educado_dec(func):

    def func_wrapper():
        #código antes de la función
        print('Buenos días')
        func()
        #código después de la
        print('Muchas gracias!')
    return func_wrapper


@educado_dec
def pregunta():
    print('¿Puedes darle un like a este video?')
@educado_dec
def respuesta():
    print('Pues claro, estoy aprendiendo un montón en este video!')

pregunta()
respuesta()
