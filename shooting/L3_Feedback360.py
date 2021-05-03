import Adafruit_BBIO.GPIO as GPIO
import L1_servo as servo
import numpy as np
import time

kp = -0.002
ki = 0.04
kd = 0.001
target = 50
position = (0,0,0)
current = 0
error = 0


def setup():
    pin = "P9_23"
    GPIO.setup(pin,GPIO.IN)
    return pin

    


def duty_cycle(pin,dutyCycle0,segment):
    pulseLow = time.time()
    pulseHigh = time.time()
    cycle = 0
    counterLow = 0
    counterHigh = 0
    while True:
        while GPIO.input(pin) == 0:
            pulseLow = time.time()
            counterLow += 1
        while GPIO.input(pin) == 1:
            pulseHigh = time.time()
            counterHigh += 1
        cycle = counterHigh + counterLow
        if 1000 < cycle < 1200:
            break
    dutyCycle1 = (counterHigh/cycle)*100
    if dutyCycle0 > 60 and dutyCycle1 < 40:
        segment += 1
    if dutyCycle0 < 40 and dutyCycle1 > 60:
        segment -= 1
    position = dutyCycle1*1.125 + segment*112.5
    return (position, dutyCycle1, segment)

def angle(pin,position,target):
    while True:
        position = duty_cycle(pin,position[1],position[2])
        current = position[0]
        error = target - current 
        if -3 < error < 3:
            break
        output = error * kp
        if output > 0.25:
            output = 0.25
        if 0 < output < 0.075:
            output = 0.075
        if -0.075 < output < 0:
            output = -0.075
        if -0.25 > output:
            output = -0.25
        #print("current:",current)
        #print("error:",error)
        #print("output:",output)
        servo.move1(output)
        time.sleep(0.05)
    servo.move1(0.0)
    return position




if __name__ == "__main__":
    setup()
    
    pin = "P9_23"
    GPIO.setup(pin,GPIO.IN)
    servo.move1(-0.2)
    dutyCycle1 = 0
    segment = 0
    x = duty_cycle(pin, dutyCycle1, segment)
    while True:
        x = angle(pin, x[1], x[2])
        print("Duty Cycle:", x)
        #print("Low:",counterLow)
        #print("High:",counterHigh)
        time.sleep(0.01)



