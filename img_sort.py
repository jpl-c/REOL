import keyboard  # using module keyboard
from PIL import Image
import os
import psutil



#path_photo_sans_tri : path vers un dossier contenant les photos à trier
#path_photo_eolienne : path vers un dossier initialement vide et qui contiendra les img avec éoliennes
#path_photo_sans_eolienne : path vers un dossier initialement vide et qui contiendr les photos sans éoliennes
path_photo_sans_tri = "C:/Users/JP/Documents/Mines/S2/Projet Info/Pytorch/Img eoliennes/Img_sans_tri/"    
path_photo_eolienne = "C:/Users/JP/Documents/Mines/S2/Projet Info/Pytorch/Img eoliennes/Img_avec_eolienne/"
path_photo_sans_eolienne = "C:/Users/JP/Documents/Mines/S2/Projet Info/Pytorch/Img eoliennes/Img_sans_eolienne/"   
listing = os.listdir(path_photo_sans_tri)   


def del_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
    else:
        print("File not found in the directory")
    #print("file deleted")



"""
When the program is run, it will loop through the pictures in the folder with unsorted images. Once the picture is opened
press r to sort it in the file with windturbines, and p if it does not have a windturbine.
The pictures are automatically moved in each folder after every key press. To quit the loop early press q
"""

flag = False
for file in listing:
    #print(file)
    im = Image.open(path_photo_sans_tri + file) 
    im.show()
    if flag :
        #print("hello")
        break 
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('r'):
                print('img has a windturbine')
                im.save(path_photo_eolienne + file, "PNG")
                for proc in psutil.process_iter():
                    if proc.name() == "display":
                        proc.kill()
                del_file(path_photo_sans_tri + file)
                break  # finishing the loop

        except:
            break  # if user pressed a key other than the given key the loop will break 

        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('p'):
                print('img does not have a windturbine')
                im.save(path_photo_sans_eolienne + file, "PNG")
                for proc in psutil.process_iter():
                    if proc.name() == "display":
                        proc.kill()
                del_file(path_photo_sans_tri + file)
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break 

        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):
                #print("hi")
                flag = True
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break  

                                     
    im.close()