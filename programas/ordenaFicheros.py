print ('Hola Mentes Ocupadas!')
home = "./../../Escritorio/Test"
# Leer la extensión de un fichero
import os
import shutil
for file in os.listdir(home):
    if file.endswith(""):
        x = (file.split("."))
        if(len(x) > 1):
            # tenemos la extensión
            extension = (x[-1])
            nombreFichero = os.path.join("", file)
            print(nombreFichero)
            print(extension)
            #Comprobar si existe un directorio con la extensión que estamos iterando
            existeDir = os.path.isdir(home+"/"+extension)
            print(home+"/"+extension)
            if(existeDir):
                print("Existe!")
                # Mueve el fichero a esta ruta
                shutil.move(((home)+"/"+nombreFichero),((home)+"/"+extension + "/" + nombreFichero))
                print("Fichero" + nombreFichero + " movido a " + ((home)+"/"+extension))
            else:
                print("NO Existe!")
                # Crea el directorio en la carpeta home con el nombre de la extensión
                os.mkdir((home)+"/"+extension)
                print("Nueva carpeta "+ extension + " creada")
                # Mueve el fichero a esta ruta
                shutil.move(((home)+"/"+nombreFichero),((home)+"/"+extension+ "/" + nombreFichero))
                print("Fichero" + nombreFichero + " movido a " + ((home)+"/"+extension))

            
            


        
