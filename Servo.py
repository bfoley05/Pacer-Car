from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(17, pin_factory=factory)

    #servo.value = -.4  # this is the middle
    #sleep(1)
    #servo.value = -.1 # this is the far left turn
    #sleep(1)
    #servo.value =  -.7 # this is the far right turn
    #sleep(5)


class Turning(): #values from 10-70
    def turn(self, x=40):
        turning = (x/-100)
        servo.value = turning
