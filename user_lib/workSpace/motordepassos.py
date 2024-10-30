from Stepper import Stepper
from time import sleep

stepsPerRevolution = 2048

# ULN2003 Motor Driver Pins
IN1 = 5 #d1
IN2 = 4 #d2
IN3 = 14 #d5
IN4 = 12 #d6

myStepper = Stepper(stepsPerRevolution, IN1, IN3, IN2, IN4)

# set the speed at 5 rpm
myStepper.setSpeed(5)

for c in range(0, 3):
    # step one revolution in one direction:
    print("clockwise")
    myStepper.step(stepsPerRevolution)
    sleep(1)
    
    # step one revolution in the other direction:
    print("counterclockwise")
    myStepper.step(-stepsPerRevolution)
    sleep(1)




