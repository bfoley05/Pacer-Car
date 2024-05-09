from MotorModule import Motor
from LaneDetectionModule import getLaneCurve
import WebcamModule
import cv2
 
##################################################
motor = Motor(2,3,4)
##################################################
 
def main():
 
    img = WebcamModule.getImg()
    curveVal= getLaneCurve(img,2)
 
    sen = 1  # SENSITIVITY this will change less is less of curve more is more
    maxVAl= 0.3 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
    if curveVal>0:
        sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    motor.moveF(0.20,-curveVal*sen,0.05)
    cv2.waitKey(1)
     
 
if __name__ == '__main__':
    while True:
        main()
