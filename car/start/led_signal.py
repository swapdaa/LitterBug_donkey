import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

red = 17
green = 27
blue = 22

Freq = 100

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)


def blink_blue():
    RED.start(0)
    GREEN.start(0)
    BLUE.start(0)
    try:
        for i in range(3):
            BLUE.ChangeDutyCycle(100)
            GREEN.ChangeDutyCycle(100)
            time.sleep(0.25)
            BLUE.ChangeDutyCycle(0)
            GREEN.ChangeDutyCycle(0)
            time.sleep(0.25)
    except:
        GPIO.cleanup()

def blink_red():
    RED.start(0)
    GREEN.start(0)
    BLUE.start(0)
    try:
        for i in range(3):
            RED.ChangeDutyCycle(100)
            time.sleep(0.25)
            RED.ChangeDutyCycle(0)
            time.sleep(0.25)
    except:
        GPIO.cleanup()

def blink_green():
    RED.start(0)
    GREEN.start(0)
    BLUE.start(0)
    try:
        for i in range(3):
            GREEN.ChangeDutyCycle(100)
            time.sleep(0.25)
            GREEN.ChangeDutyCycle(0)
            time.sleep(0.25)
    except:
        GPIO.cleanup()

