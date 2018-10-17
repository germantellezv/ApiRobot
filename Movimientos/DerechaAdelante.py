import RPi.GPIO as GPIO
import os
import time

ena = 18
in1 = 23
in2 = 24
enb = 19
in3 = 6
in4 = 5
GPIO.setmode(GPIO.BCM)

GPIO.setup(ena,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

GPIO.setup(enb,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

pwm_a = GPIO.PWM(ena,500) # 500Hz es la frecuencia del motor
pwm_b = GPIO.PWM(enb,500) #

pwm_a.start(0)   # Se inicia el motor con un 0% de esfuerzo o Duty Cycle
pwm_b.start(0)  # Descomentar esta linea para inicializar el motor en 0% de esfuerzo
os.system('clear')


try:
        while True:
		GPIO.output(in1,False)
		GPIO.output(in2,True)
		GPIO.output(in3,False)
                GPIO.output(in4,True)
                pwm_a.ChangeDutyCycle(100)
		pwm_b.ChangeDutyCycle(0)


except KeyboardInterrupt:
        pwm_a.stop()
        pwm_b.stop()
        GPIO.cleanup()
        os.system('clear')
        print
        print("Programa Terminado por el usuario")
        print
        exit()
