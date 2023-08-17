import RPi.GPIO as GPIO
import time

servoPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:
    p.ChangeDutyCycle(6)
    time.sleep(2)
    p.ChangeDutyCycle(10)
    time.sleep(2)
    p.ChangeDutyCycle(6)
    time.sleep(2)
    p.stop()
   
   
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
