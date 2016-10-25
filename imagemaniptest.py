import urllib
from PIL import Image

width = int(raw_input("Enter width: "))
height = int(raw_input("Enter height: "))
thumbwidth = 16*(height/9)
count = int(raw_input("Number of images: "))
blur = ""
if (raw_input("Blur the images?(y,n) ")=="y"):
    blur = "&blur"
else: blur = ""
i=0

while (i < count):
    URL = "http://www.unsplash.it/%d/%d/?random%s"%(width,height,blur)
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
