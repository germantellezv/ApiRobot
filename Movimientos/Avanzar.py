import RPi.GPIO as GPIO
import os
import time

# GPIO pin defintions
ena = 18
in1 = 23
in2 = 24
enb = 19
in3 = 6
in4 = 5

# Configure GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(ena,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

GPIO.setup(enb,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

pwm_a = GPIO.PWM(ena,500)  
pwm_b = GPIO.PWM(enb,500) 

pwm_a.start(0)   
pwm_b.start(0)  
os.system('clear')

# Start the motor running
GPIO.output(in1,False)
GPIO.output(in2,True)
GPIO.output(in3,False)
GPIO.output(in4,True)
pwm_a.ChangeDutyCycle(100)
pwm_b.ChangeDutyCycle(100)

# Wait five seconds
try:
    time.sleep(5)

# In case the user presses CTRL+C
except KeyboardInterrupt:
        print("User finished the program")

# If we get here, either five seconds has passed, or the user pressed CTRL+C.  Either way, stop the motor and clean up
pwm_a.stop()
pwm_b.stop()
GPIO.cleanup()
os.system('clear')

exit()
