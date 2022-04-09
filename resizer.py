from PIL import Image
import os
from glob import glob

path = "C:/Users/CoDeAgGrEsSiVe/Downloads/General/General"
HEIGHT = 200
WIDTH = 200

def resize():
    ext = ['png', 'jpg', 'gif']
    for e in ext:
        for item in glob(path + '/*.' + e):
                im = Image.open(item)
                print(im)
                fileName, extension = os.path.splitext(item)
                imResize = im.resize((HEIGHT,WIDTH), Image.ANTIALIAS)
                imResize.save(fileName + '.png', 'PNG', quality=90)
resize()