import glob
import os
import PIL
from PIL import Image




def Flip(foto):
    im = Image.open(foto).convert('RGB')
    im = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    new_filename = os.path.splitext(foto)[0]
    #new_filename = new_filename  + ".jpg" + "_flipped"
    new_filename = new_filename  + ".jpg"
    im.save(new_filename)
    im.show()  


if __name__ == "__main__":
    dirName = 'C:\\Users\\vudan\\OneDrive\\Desktop\\Automation Project\\Odontology\\Flip-image\\test'
    #saveLocation = 'C:\\Users\\vudan\\OneDrive\\Desktop\\Automation Project\\Odontology\\Flip-image\\Flipped'
    #savePath = os.pardir(saveLocation)
    allFiles = list()
    listofFile = os.listdir(dirName)
    for files in listofFile:
        fullPath = os.path.join(dirName,files)
        allFiles.append(fullPath)
        #print(allFiles)
    Flip(allFiles[1]) 
