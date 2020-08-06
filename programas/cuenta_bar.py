class Cuenta:

    menu = {
        'vino':4,
        'cerveza':3,
        'refresco':2,
        'pollo':10,
        'carne':15,
        'ensalada':12,
        'postre':6
    }

    def __init__(self):
        self.total = 0
        self.objetos = []

    def add(self,objeto):
        self.objetos.append(objeto)
        self.total += self.menu[objeto]

    def print_factura(self,impuesto,servicio):
        impuesto = (impuesto/100)*self.total
        servicio = (servicio/100)*self.total
        total = self.total + impuesto + servicio

        for objeto in self.objetos:
            print(f'{objeto:20} €{self.menu[objeto]}')

        print(f'{"Total":20} €{total:.2f}')
