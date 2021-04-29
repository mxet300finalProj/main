# This program is used for stabbing

# Import Internal Programs
#import L2_log as log
#import L1_motors as mot


# Import External Programs
# motor
#import rcpy
#import rcpy.motor as motor
import time                                     # only necessary if running this program as a loop
import numpy as np                              # for clip function
#import L2_speed_control as sc
#import L2_inverse_kinematics as inv
import L2_loop_drive as drive
#import Lab6Template as lab
# import L1_lidar as lidar

# motor
#motor_l = 1 	                                # Left Motor (ch1)
#rcpy.set_state(rcpy.RUNNING)                    # initialize the rcpy library for both motor and servo
timeL = 2                                       # 2 seconds
print("yo")
# Run the main loop
if __name__ == "__main__":
    # need distance and angle 
    # by setting how much time will be used to divide the distance and angle difference
    # this will get the velocity and theta_dot (rad/s)
    # x_dot will be the quation of x_dot = (D*|Theta2-Theta1|)/time
    # then use theta_dot = R/2L * (prd - pld)
    # x_dot = R/2 * (prd + pld)
    # these equations solve for prd and pld they need to be rearranged
    
    # using the given angle from the lidar sensor turn the SCUTTLE
    #myVelocities = np.array([0, 9999]) #input angle in second position
	#myPhiDots = inv.convert(myVelocities)
	#kin.getPdCurrent() # capture latest phi dots & update global var
    #pdCurrents = kin.pdCurrents # assign the global variable value to a local var
    
    #
    # actualy use L2_loop_drive.py, its the same as Lab6Template.py but change
    # the phitargets using some of the code above, meaning take in angle from lidar
    # then use this to turn scuttle
    #
    x = 0.5 # distance recived from lidar
    th = 30 # angle from lidar
    # get distance from lidar and convert to m/s, time is 2 seconds
    x_d = x / timeL
    # get angle from lidar and convert to rad/s, time is 2 seconds
    theta_d = (th * (np.pi/180)) / timeL
    print("did x_d and theta_d")
    # SCUTTLE drives to target
    drive.loop_drive(x_d, theta_d, x, th)
    #lab.loop_drive()
	# drive.rev_loop_drive() # SCUTTLE reverses to original position
	
	
