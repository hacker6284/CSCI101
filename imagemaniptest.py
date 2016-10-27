import urllib
from PIL import Image
from PIL import ImageFilter
import Tkinter as tk
import tkFileDialog
import sys

random = raw_input("Do you have an image?(y/n) ")
if (random == "y"):
    root = tk.Tk()
    root.update()
    root.withdraw()
    file_path = tkFileDialog.askopenfilename(title="Choose Image")
    root.deiconify()
    root.update()
    root.destroy()
    root.quit()
    background = Image.open(file_path)
    width,height = background.size
    count = 1
else:
    width = int(raw_input("Enter width: "))
    height = int(raw_input("Enter height: "))
    count = int(raw_input("Number of images: "))
    
thumbwidth = 16*(height/9)
thumbheight = 9*(width/16)

i=0

save = tk.Tk()
save.update()
save.withdraw()
savedir = tkFileDialog.askdirectory(title="Choose Save Location")
save.deiconify()
save.update()
save.destroy()
save.quit()

while (i < count):
    if (random != "y"): 
        URL = "http://www.unsplash.it/%d/%d/?random"%(width,height)
        urllib.urlretrieve(URL, "imagetests/%d.png"%(i))
        background = Image.open("imagetests/%d.png"%(i))
        
    overlay = Image.open("imagetests/wallpapertemplate.png")
    
    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    background2 = background.filter(ImageFilter.GaussianBlur(10))

    #overlay = overlay.resize((thumbwidth,height))
    newwidth,newheight = overlay.size
    
    background.paste(overlay, (0-(newwidth-width)/2,0-(newheight-height)/2), overlay)
    background2.paste(overlay, (0-(newwidth-width)/2,0-(newheight-height)/2), overlay)
    background.load()
    background.save("%s/%d_noblur.png"%(savedir,i),"PNG")
    background2.load()
    background2.save("%s/%d.png"%(savedir,i),"PNG")

    #overlay.crop((newwidth/2-width/2,newheight/2+height/2,newwidth/2+width/2,newheight/2-height/2))
    #background2.paste(background, (0, 0), overlay)
    #background2.save("imagetests/%d_blur_triangle.png"%(i), "PNG")

    i += 1

