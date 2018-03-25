from picamera import PiCamera
from time import sleep
import os


camera = PiCamera()
os.remove('/home/pi/Desktop/CameraCapture.jpg')
camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/CameraCapture.jpg')
camera.stop_preview()
fileObject.close()
