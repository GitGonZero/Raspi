import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
while True:
    while True:
        inputValue = GPIO.input(25)
        if (inputValue == True):
            os.system('sudo gpio -g mode 24 in')
            GPIO.output(17, GPIO.HIGH)
            print("Encendido")
            time.sleep(0.3)
            break
    while True:
        inputValue = GPIO.input(25)
        if (inputValue == True):
            os.system('sudo gpio -g mode 24 out')
            GPIO.output(17, GPIO.LOW)
            print("Apagado")
            time.sleep(0.3)
            break
    #GPIO.cleanup()
#i=0
#while True:
#    i=i+1
#    time.sleep(1)
