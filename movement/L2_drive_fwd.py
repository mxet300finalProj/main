# Import Internal Programs
import L2_log as log
import L1_motors as mot

import time                                     # only necessary if running this program as a loop
import numpy as np                              # for clip function

import L2_displacement as dis



# Run the main loop
def driving(travel):
    x = 0
    t = 0
    encL1 = 0 
    encR1 = 0
    while(1):
        dist = travel
        print("motors.py: driving fwd")
        x, t, encL1, encR1 = dis.distAchieved(x, t, encL1, encR1)
        if (x >= dist):
            print("distance traveld: ", x)
            print("Angle Turned:", t)
            print("Driving finished")
            mot.MotorL(0)                         # gentle speed for testing program. 0.3 PWM may not spin the wheels. # run motor
            mot.MotorR(0)
            # time.sleep(1)
            break
        print("x:", x)
        print("driving")
        mot.MotorL(0.831)                         # gentle speed for testing program. 0.3 PWM may not spin the wheels. # run motor
        mot.MotorR(0.8)

if __name__ == "__main__":
    driving(0.5)