import urllib
from PIL import Image

height = int(raw_input("Enter height: "))
width = int(raw_input("Enter width: "))
thumbwidth = 16*(height/9)
count = int(raw_input("Number of images: "))
i=0

while (i < count):
    URL = "http://www.unsplash.it/%d/%d/?random"%(width,height)
    urllib.urlretrieve(URL, "imagetests/%d.png"%(i))
    
    background = Image.open("imagetests/%d.png"%(i))
    overlay = Image.open("imagetests/wallpapertemplate.png")
    
    
    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    overlay.thumbnail([max(thumbwidth, width),max(thumbwidth, width)])
    newwidth,newheight = overlay.size
    background.paste(overlay, (0-(newwidth-width)/2,0-(newheight-height)/2), overlay)
    background.load()
    background.save("imagetests/%d.png"%(i),"PNG")

    i += 1
