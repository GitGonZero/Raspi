import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN)
hora = time.strftime("%H:%M:%S")
fecha = time.strftime("%d/%m/%y")
#GPIO.setup(24, GPIO.OUT)

try:
        time.sleep(2)
        print fecha, hora,("|==>: Iniciando.")
        #print(time.strftime("%H:%M:%S"))
        #print("iniciando")
        while True:
            if GPIO.input(7):
                #GPIO.output(24, True)
                #time.sleep(0.5)
                #GPIO.output(24, False)
                print fecha, hora, ("|==>: Movimiento detectado,foco encendido.")
                os.system('sh /home/pi/scripts/focoOn.sh')
                time.sleep(5.5)
                time.sleep(0.1)
                #os.system('sh /home/pi/scripts/focoOff.sh')
                # print("estado original")

            else:
                os.system('sh /home/pi/scripts/focoOff.sh')
                print fecha, hora, ("|==>: Foco apagado.")
                time.sleep(5.5)
except:
    GPIO.cleanup()

