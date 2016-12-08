import urllib
from PIL import Image
from PIL import ImageFilter
import sys

random = raw_input("Do you have an image?(y/n) ")
if (random == "y"):
    file_path = raw_input("What is the path of your image?")
    background = Image.open(file_path)
    width,height = background.size
    count = 1
else:
    width = int(raw_input("Enter width: "))
    height = int(raw_input("Enter height: "))
    count = int(raw_input("Number of images: "))
    
thumbwidth = int(16*(height/9))
thumbheight = int(9*(width/16))

i=0

savedir = raw_input("What is the desired save directory?")

mode = int(raw_input("Mode(0=default,1=noblur,2=onlyblur,3=pixelate,4=pixelatebackground)"))

while (i < count):
    if (random != "y"): 
        URL = "http://www.unsplash.it/%d/%d/?random"%(width,height)
        urllib.urlretrieve(URL, "imagetests/%d.png"%(i))
        background = Image.open("imagetests/%d.png"%(i))
        
    overlay = Image.open("imagetests/wallpapertemplate.png")
    
    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    background2 = background.filter(ImageFilter.GaussianBlur(10))

    #if (mode > 2):
        #pixelback = background.resize((width/10,height/10))
        #pixelback2 = pixelback.resize((width,height))
        
    overlay = overlay.resize((thumbwidth,height))
    newwidth,newheight = overlay.size
   
    if (mode == 0 or mode == 1):
        background.paste(overlay, (0-(newwidth-width)/2,0-(newheight-height)/2), overlay)
        background.save("%s/%d_noblur.png"%(savedir,i),"PNG")
    if (mode == 0 or mode == 2):
        background2.paste(overlay, (0-(newwidth-width)/2,0-(newheight-height)/2), overlay)
        background2.save("%s/%d.png"%(savedir,i),"PNG")
    if (mode == 3):
        background.paste(overlay, (0-(newwidth-width)/2,0-(newheight-height)/2), overlay)
        pixelback = background.resize((width/10,height/10))
        pixelback = pixelback.resize((width,height))
        pixelback.save("%s/%d_pixel.png"%(savedir,i),"PNG")
    if (mode == 4):
        pixelback = background.resize((width/10,height/10))
        pixelback = pixelback.resize((width,height))
        pixelback.paste(overlay, (0-(newwidth-width)/2,0-(newheight-height)/2), overlay)
        pixelback.save("%s/%d_pixelback.png"%(savedir,i),"PNG")

    #overlay.crop((newwidth/2-width/2,newheight/2+height/2,newwidth/2+width/2,newheight/2-height/2))
    #background2.paste(background, (0, 0), overlay)
    #background2.save("imagetests/%d_blur_triangle.png"%(i), "PNG")

    i += 1

