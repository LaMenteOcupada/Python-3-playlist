class Planeta:

    def __init__(self,nombre,radio,gravedad,sistema):
        self.nombre = nombre
        self.radio = radio
        self.gravedad = gravedad
        self.sistema = sistema

    def orbita(self):
        return f'{self.nombre} está orbitando en el sistema {self.sistema}'

marte = Planeta('Marte',6790,3.2,'Solar')
print(f'Nombre es : {marte.nombre}')
print(f'Radio es : {marte.radio}')
print(f'La gravedad es : {marte.gravedad}')
print(marte.orbita())

tierra = Planeta('Tierra',13000,9.2,'Solar')
print(f'Nombre es : {tierra.nombre}')
print(f'Radio es : {tierra.radio}')
print(f'La gravedad es : {tierra.gravedad}')
print(tierra.orbita())
