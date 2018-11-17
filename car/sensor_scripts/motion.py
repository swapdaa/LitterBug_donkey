import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pir_sensor = 4

GPIO.setup(pir_sensor, GPIO.IN, GPIO.PUD_DOWN)

current_state = 0

try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
          print("GPIO pin %s is %s" % (pir_sensor, current_state)) # motion detected
          print("DETECTED YOU!")
          time.sleep(2) # wait 1 seconds for PIR to reset. 
        else:
          print("Nothing!!")
except KeyboardInterrupt:
    GPIO.cleanup()
