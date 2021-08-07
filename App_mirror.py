#Date: 20th July, 2020
#Dang Thai Hai Vu _ Author
#Email: vudang2414@gmail.com
#Odontology project with DDS. Nguyen Dac Bao Chinh (DDS at HT Smile)
#Type: include mirror
from tkinter import * 
from tkinter import messagebox
import glob
import os
import PIL
from PIL import Image

# Notification GUI
def notibox():
    window = Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()

    messagebox.showinfo('HT_Smile','Task has been done !')

    window.deiconify()
    window.destroy()
    window.quit()

# Lower Jaw: Flip and Rotate 180 deg
def Lower_Jaw(foto):
    im = Image.open(foto)
    img = im.transpose(PIL.Image.FLIP_LEFT_RIGHT).rotate(180)
    dst = os.path.splitext(foto)[0] + " flipped" + ".jpg"
    img.save(foto)
    os.rename(foto,dst)

# Upper Jaw: Flip
def Upper_Jaw(foto):
    im = Image.open(foto).convert('RGB')
    img = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    dst = os.path.splitext(foto)[0] + " flipped" + ".jpg"
    img.save(foto)
    os.rename(foto,dst)

# Left Jaw: Flip
def Left_Jaw(foto):
    im = Image.open(foto).convert('RGB')
    img = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    dst = os.path.splitext(foto)[0] + " flipped" + ".jpg"
    img.save(foto)
    os.rename(foto,dst)

# Right Jaw: Flip
def Right_Jaw(foto):
    im = Image.open(foto).convert('RGB')
    img = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    dst = os.path.splitext(foto)[0] + " flipped" + ".jpg"
    img.save(foto)
    os.rename(foto,dst)


if __name__ == "__main__":
    #Path of the source data:
    dirName = 'C:\\Users\\vudan\\OneDrive\\Desktop\\Automation Project\\Odontology\\Flip-image\\images'
    #Create list that keeps the foto
    allFiles = list()
    listofFile = os.listdir(dirName)
    listofFile.sort()
    for files in listofFile:
        fullPath = os.path.join(dirName,files)
        allFiles.append(fullPath)
    
    #Start to rotate foto, this loop will run through each case resprectively 
    # and repeat until it reach the last foto
    i=0
    print(allFiles)
    while i < (len(allFiles)):
        #No3_Lower_Jaw
        i += 4
        Lower_Jaw(allFiles[i]) 
        #No4_Upper_Jaw
        i += 1
        Upper_Jaw(allFiles[i])
        if i == len(allFiles):
            break
        i += 1
    #Notification box
    notibox()
   
