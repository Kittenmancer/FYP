#Code modified from tutorial found at https://www.modmypi.com/blog/raspberry-pi-gpio-sensing-motion-detection
import RPi.GPIO as GPIO
import time
import os
from picamera import PiCamera

GPIO.setmode(GPIO.BCM) 

IR_PIN = 4

GPIO.setup(IR_PIN, GPIO.IN)
camera = PiCamera()

try:
    print("Motion sensor camera capture enabled")
    time.sleep(2)
    while True:
        if GPIO.input(IR_PIN):
            print("Capturing image")
            #os.remove('/home/pi/Desktop/CameraCapture.jpg')
            camera.start_preview()
            time.sleep(3)
            camera.capture('/home/pi/Desktop/CameraCapture.jpg')
            camera.stop_preview()
            print("Image captured")
            time.sleep(20)
            print("Camera ready")
            

except KeyboardInterrupt:
    print ("Motion sensor camera capture disabled")
    GPIO.cleanup()
