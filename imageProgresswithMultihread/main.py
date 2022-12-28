import multiprocessing 
import numpy as np
from PIL import Image


def get_image(image_path):
    
         """Get a numpy array of an image so that one can access values[x][y]."""
         image = Image.open(image_path, "r")
         width, height = image.size
         pixel_values = list(image.getdata())
         if image.mode == "RGB":
             channels = 3
         elif image.mode == "L":
             channels = 1
         else:
             print("Unknown mode: %s" % image.mode)
             return None
         pixel_values = np.array(pixel_values).reshape((width, height, channels))
         return pixel_values
 




if __name__=="__main__":
    #put your picture path
    imags="/home/damlayasarr/Downloads/photo1668523621.jpeg"
    process=multiprocessing.Process(target=get_image, args=(imags,))
    process.start()
    process.join()
    print(process)
    result=get_image(imags)
    print(result[0])
   



