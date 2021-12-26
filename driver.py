import RPi.GPIO as GPIO
from time import sleep
import os
LED_POWER = 15
LED_PIR = 13
LED_MLX = 29
LED_MASK = 31
LED_FACE = 16
PIR_input = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_input, GPIO.IN)	
GPIO.setup(LED_POWER, GPIO.OUT)
GPIO.output(LED_POWER, GPIO.LOW)
GPIO.setup(LED_PIR, GPIO.OUT)
GPIO.output(LED_PIR, GPIO.LOW)
GPIO.setup(LED_MASK, GPIO.OUT)
GPIO.output(LED_MASK, GPIO.LOW)
GPIO.setup(LED_FACE, GPIO.OUT)
GPIO.output(LED_FACE, GPIO.LOW)
GPIO.setup(LED_MLX, GPIO.OUT)
GPIO.output(LED_MLX, GPIO.LOW)
GPIO.output(LED_POWER, GPIO.HIGH)

while True:
    if(GPIO.input(PIR_input)):
        GPIO.output(LED_PIR, GPIO.HIGH)
        os.system('python3 /home/pi/tensorflow/Final_Codes/Mask/testing.py')
        GPIO.output(LED_MASK, GPIO.HIGH)
        os.system('python3 /home/pi/tensorflow/Final_Codes/Recognition_Final/testing.py')
        GPIO.output(LED_FACE, GPIO.HIGH)
        sleep(2)
        os.system('python3 /home/pi/tensorflow/Final_Codes/temperature_measurement.py')
        GPIO.output(LED_MLX, GPIO.HIGH)
        os.system('python3 /home/pi/tensorflow/Final_Codes/servo.py')
        GPIO.output(LED_MLX, GPIO.LOW)
        sleep(1)
        GPIO.output(LED_FACE, GPIO.LOW)
        sleep(1)
        GPIO.output(LED_MASK, GPIO.LOW)
    else:
        GPIO.output(LED_PIR, GPIO.LOW)



