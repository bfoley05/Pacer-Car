from MotorModule import Motor
import JoyStickModule as js
from time import sleep
 
motor= Motor(2,3,4)
 
def main():
    jsVal = js.getJS()
    speed = jsVal['axis2']*100
    value = jsVal['axis3']
    print(speed)
    turns = map_value(value, 0, 1, 40, 70)
    if speed<0:
        motor.moveF(x=(-1*speed), turn=turns, t=0.1)
    else:
        motor.moveB(x=speed, turn=turns, t=0.1)
    
    #motor.moveF(t=3)
    #motor.stop(2)
    #motor.moveB(t=3)
    #motor.stop(2)
 
def map_value(value, from_min, from_max, to_min, to_max):
    # Calculate the ratio of the input value's position within the input range
    ratio = (value - from_min) / (from_max - from_min)
    # Map the ratio to the output range
    mapped_value = to_min + ratio * (to_max - to_min)
    return mapped_value



if __name__ == '__main__':
    while True:
        main()
