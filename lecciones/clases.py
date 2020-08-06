from espacio.planeta import Planeta
from espacio.calc import masa_planeta,vol_planeta

tierra = Planeta('Tierra',13000,9.2,'Solar')

masa_tierra = masa_planeta(tierra.gravedad , tierra.radio)
vol_tierra = vol_planeta(tierra.radio)

print(f'{tierra.nombre} tiene una masa de {masa_tierra} y un volumen de {vol_tierra}')
