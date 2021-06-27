import os
home = "./../../Escritorio/Test"
#myFile = open(home+"/new.txt", "w+")

extensiones = ["jpg","pdf","mov","mp3","mp4","aac","zip","rar","epub"]
for ext in extensiones:
    myFile1 = open(home+"/fichero6."+ext, "w+")
    myFile2 = open(home+"/fichero7."+ext, "w+")
    myFile3 = open(home+"/fichero8."+ext, "w+")
    myFile4 = open(home+"/fichero9."+ext, "w+")
    myFile5 = open(home+"/fichero10."+ext, "w+")