import RPi.GPIO as GPIO
import serial
import time
import os
#asiganacion a variables de puerto de comunicacion Arduino
arduino = serial.Serial('/dev/ttyACM0',9600)
#Establecer modo de pines BCM e identificacion de los mismos
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(26, GPIO.IN)
##Creacion de las variables (flags) que controlarn si los sistemas estan encendidos o apagados (se les asigna valor cero)
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5 = 0
flag6 = 0
flag7 = 0
flag8  = 0
flag9 = 0
#lineas para log
print('Iniciado programa de control de sistemas de iluminacion:')
#Inicio del bucle principal que permite ejecucin permanente
while True:
	#Asignacion de las entradas GPIO a las variables de control de encendido de cada sistema
	input_state1 = GPIO.input(5)
	input_state2 = GPIO.input(12)
	input_state3 = GPIO.input(6)
	input_state4 = GPIO.input(13)
	input_state5 = GPIO.input(19)
	input_state6 = GPIO.input(16)
	input_state7 = GPIO.input(26)
	input_state8 = GPIO.input(20)
	input_state9 = GPIO.input(21)
	#bucle control Led 1
	#Encendido
	if input_state1 == True and flag1 == 0:
		arduino.write('1H')
		print('encendido sistema 1')
		flag1 = 1
		time.sleep(0.3)
	#Apagado
        else:
            if input_state1 == True and flag1 == 1:
		arduino.write('1L')
		print('apagado sistema 1')
		time.sleep(0.3)
	#Bucle control sistema2
	#Encendido
	if input_state2 == True and flag2 == 0:
		arduino.write('2H')
		print('encendido sistema 2')
		flag2 = 1
		time.sleep(0.3)
	#Apagado
        else:
            if input_state2 == True and flag2 == 1:
		arduino.write('2L')
		print('apagado sistema 2')
		flag2 = 0
		time.sleep (0.3)
	#Bucle control sistema3
	#Encendido
	if input_state3 == True and flag3 == 0:
		arduino.write('3H')
		print('encendido el sistema 3')
		flag3 = 1
		time.sleep(0.3)
	#apagado
        else:
            if input_state3 == True and flag3 == 1:
		arduino.write('3L')
		print('apagado sistema 3')
		flag3 = 0
		time.sleep (0.3)
	#Bucle control sistema 4
	#Encendido
	if input_state4 == True and flag4 == 0:
		arduino.write('4H')
		print('encendido sistema 4')
		flag4 = 1
		time.sleep(0.3)
	#Apagado
        else:
            if input_state4 == True and flag4 == 1:
		arduino.write('4L')
		print('apagado sistema 4')
		flag4 = 0
		time.sleep (0.3)
	#Bucle control de sistema 5
	#Encendido
	if input_state5 == True and flag5 == 0:
		arduino.write('5H')
		print('encendido sistema 5')
		flag5 = 1
		time.sleep(0.3)
	#Apagado
	else:
            if input_state5 == True and flag5 == 1:
		arduino.write('5L')
		print('apagado sistema5')
		flag5 = 0
		time.sleep (0.3)
	#Bucle control sistema 6
	#Encendido
	if input_state6 == True and flag6 == 0:
		arduino.write('6H')
		print('encendido sistema 6')
		flag6 = 1
		time.sleep(0.3)
	#Apagado
        else:
            if input_state6 == True and flag6 == 1:
		arduino.write('6L')
		print('apagado sistema6')
		flag6 = 0
		time.sleep (0.3)
	#Bucle control sistema 7
	#Encendido
	if input_state7 == True and flag7 == 0:
		arduino.write('7H')
		print('encendido sistema 7')
		flag7 = 1
		time.sleep(0.3)
	#apagado
        else:
            if input_state7 == True and flag7 == 1:
		arduino.write('7L')
		print('apagado sistema 7')
		flag7 = 0
		time.sleep (0.3)
	#Bucle control de sistema 8
	#encendido
	if input_state8 == True and flag8 == 0:
		arduino.write('8H')
		print('encendido sistema 8')
		flag8 = 1
		time.sleep(0.3)
	#apagado
        else:
            if input_state8 == True and flag8 == 1:
		arduino.write('8L')
		print('apagado sistema 8')
		flag8 = 0
		time.sleep (0.3)
	#Bucle control sistema 9
	#Encendido
	if input_state9 == True and flag9 == 0:
		arduino.write('9H')
		print('encendido sistema 9')
		flag9 = 1
		time.sleep(0.3)
	#Apagado
        else:
            if input_state9 == True and flag9 == 1:
		arduino.write('9L')
		print('apagado sistema 9')
		flag9 = 0
		time.sleep (0.3)

