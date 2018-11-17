#!/usr/bin/env python3
from time import sleep
import subprocess as sp
from joystick import JoystickController

DEVICE_ID = "60:38:0E:ED:1E:E7"

def control_checker(device):
    found = False
    while not found:
        stdoutdata = sp.getoutput("hcitool con")
        if device in stdoutdata.split():
            found = True
        else:
            sleep(1)
    return found

if __name__ == "__main__":
    flag = control_checker(DEVICE_ID)
    if flag:
        js = JoystickController()
        js.update()

