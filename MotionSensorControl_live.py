#Code modified from tutorial found at https://www.modmypi.com/blog/raspberry-pi-gpio-sensing-motion-detection
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 

IR_PIN = 4

GPIO.setup(IR_PIN, GPIO.IN)

try:
    print("Motion sensor camera capture enabled")
    time.sleep(2)
    while True:
        if GPIO.input(IR_PIN):
            execfile("PiCamCapture_live.py")
        time.sleep(20)

except KeyboardInterrupt:
    print ("Motion sensor camer capture disabled")
    GPIO.cleanup()
