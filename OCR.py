import numpy as np
from PIL import ImageGrab,Image,ImageOps
import cv2
import time
import pytesseract

box =(626,298,1437,850)

def ORC():
    img = Image.open('discord\discord.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    result = pytesseract.image_to_string(img)

    with open('discord.txt', mode="w") as file:
        file.write(result)
        file.close()
       # print(result)
        print("ORC-complete")
def SHOT(box):
    img = ImageGrab.grab(bbox=(box))
    grey = ImageOps.grayscale(img)
    grey.save('discord\discord.png')



def screen_record():
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        printscreen = np.array(ImageGrab.grab(bbox=(760,584,1393,792)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

