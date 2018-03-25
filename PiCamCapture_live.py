from picamera import Picamera
from time import sleep
import os

camera = Picamera()

camera.start_preview()
os.remove('/home/pi/Desktop/CameraCapture.jpg', ignore_errors = true)
sleep(3)
camera.capture('/home/pi/Desktop/CameraCapture.jpg')
camera.stop_preview()
