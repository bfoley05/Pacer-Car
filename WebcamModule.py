import cv2
import numpy as np
 
cap = cv2.VideoCapture('Track.mp4')
 
def getImg(display= False,size=[480,240]):
    _, img = cap.read()
    img = cv2.resize(img, (480, 240))
    if display:
        cv2.imshow('IMG',img)
    return img
 
if __name__ == '__main__':
    while True:
        img = getImg(True)
