# This program is used for shooting the poker chips using OUT 1 & OUT 2 on 2nd Motor Driver

# Import Internal Programs
import L2_log as log
import L1_motors as mot
import L1_servo as serv


# Import External Programs
# motor
import rcpy
import rcpy.motor as motor
import time                                     # only necessary if running this program as a loop
import numpy as np                              # for clip function
# servo
import rcpy.servo as servo
import rcpy.clock as clock	# For PWM period for servos

# motor
motor_l = 1 	                                # Left Motor (ch1)
rcpy.set_state(rcpy.RUNNING)                    # initialize the rcpy library for both motor and servo

# servo
duty = 1.5		# Duty cycle (-1.5,1.5 is the typical range)
period = 0.02 	# recommended servo period: 20ms (this is the interval of commands)
ch1 = 1			# select channel (1 thru 8 are available)

srvo1 = servo.Servo(ch1)	# Create servo object
clck1 = clock.Clock(srvo1, period)	# Set PWM period for servos
servo.enable()		# Enables 6v rail on beaglebone blue
clck1.start()		# Starts PWM

# Run the main loop
if __name__ == "__main__":
    while rcpy.get_state() != rcpy.EXITING:     # exit loop if rcpy not ready
        if rcpy.get_state() == rcpy.RUNNING:    # execute loop when rcpy is ready
            # motor
            print("motors.py: driving fwd")
            mot.MotorL(0.6)                         # gentle speed for testing program. 0.3 PWM may not spin the wheels. # run motor
            time.sleep(2)
            # servo
            print("move 1.0")
            serv.move1(1.0)	# Set servo duty (1.0 has no units, see library for details) (60 degrees)
            time.sleep(0.2) # short delay
            print("move -1.0")
            serv.move1(-1.0)
            time.sleep(0.2)  # short delay
            #time.sleep(2)  # 2 seconds delay
            mot.MotorL(0)
            time.sleep(2)
			
			# return servo turret to center
			#### need code here