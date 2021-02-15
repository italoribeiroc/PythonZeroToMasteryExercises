import sys
import os
from PIL import Image

#Grab first and second argument
pasta = sys.argv[1]
novaPasta = sys.argv[2]
#check is /new exists, if not create
diretorio = "./"+ novaPasta
if not os.path.exists(novaPasta):
    os.makedirs(diretorio)
#loop through Pokedex
for arquivo in os.listdir(pasta):
    fileName =  os.path.splitext(arquivo)[0]
    img = Image.open(f"{pasta}{arquivo}")
    #convert images to png
    local = f"{diretorio}{fileName}.png"
    #save to the new folder
    img.save(local, format="PNG")
print("All done!")
