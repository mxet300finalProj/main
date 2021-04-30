# Import Internal Programs
import L2_log as log
import L1_motors as mot

import time                                     # only necessary if running this program as a loop
import numpy as np                              # for clip function

import L2_displacement as dis
import L2_heading as head


# Run the main loop
def turning(angle):
    if (angle < 0):
        LR = 1
    elif (angle > 0):
        LR = 0
    h = round(head.getHeading(head.scale(head.getXY()))*180/np.pi, 2)
    print("heading angle: ", h)
    tar = h - angle
    x = 0
    t = 0
    encL1 = 0 
    encR1 = 0
    while(1):
        he = round(head.getHeading(head.scale(head.getXY()))*180/np.pi, 2)
        print("my heading angle", he)
        print("target angle: ", tar)
        print("my angle", angle)
        turned = angle
        print("turning now")
        x, t, encL1, encR1 = dis.distAchieved(x, t, encL1, encR1)
        print("current angle: ", t)
        if (LR == 0): # turning left
            if (t >= turned/100): # (he <= tar
                print("distance traveld: ", x)
                print("Angle Turned:", t)
                print("Driving finished")
                # time.sleep(1)
                print("turned left")
                mot.MotorR(0.0)
                mot.MotorL(0.0)
                time.sleep(1)
                break
        elif (LR == 1): # turning right
            if (t <= turned/100):
                print(t)
                print("distance traveld: ", x)
                print("Angle Turned:", t)
                print("Driving finished")
                # time.sleep(1)
                print("turned right")
                mot.MotorR(0.0)
                mot.MotorL(0.0)
                time.sleep(1)
                break
        else:
            print("You are missing the second argument")
            break
        
        print("x:", x)
        print("turning")
        if (angle > 0): # turning left
            mot.MotorR(0.6)
            mot.MotorL(-0.631)
        elif (angle < 0): # turning right
            mot.MotorL(0.631)
            mot.MotorR(-0.6)
        

if __name__ == "__main__":
    h = round(head.getHeading(head.scale(head.getXY()))*180/np.pi, 2)
    print("heading angle: ", h)
    turning(45)
    
    turning(-45)
    turning(-45)
    
    turning(45)
    
    
    #time.sleep(0.02)
    #turning(-45, 1) # if you want to turn 180 don't put in 180 do another turning function with 90 degrees