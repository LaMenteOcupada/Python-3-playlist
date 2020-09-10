import urllib.request

def desc_jpg(url,ruta_fichero,nombre_fichero):
    ruta_completa = ruta_fichero + nombre_fichero + '.jpg'
    urllib.request.urlretrieve(url,ruta_completa)

url = input('Introduce la URL de la imagen:')
nombre_fichero = input('INtroduce el nombre de la imagen:')

desc_jpg(url, 'imagenes/', nombre_fichero)
