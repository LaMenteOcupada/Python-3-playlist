class Planeta:

    forma = 'redondos'

    def __init__(self,nombre,radio,gravedad,sistema):
        self.nombre = nombre
        self.radio = radio
        self.gravedad = gravedad
        self.sistema = sistema

    def orbita(self):
        return f'{self.nombre} está orbitando en el sistema {self.sistema}'

    @classmethod
    def commons(cls):
        return f'Todos los planetas son {cls.forma} por la gravedad'

    @staticmethod
    def giro(velocidad = '3000 km/h'):
        return f'El planeta gira y gira a {velocidad}'

tierra = Planeta('Tierra',13000,9.2,'Solar')

print(tierra.giro('mucha velocidad'))
