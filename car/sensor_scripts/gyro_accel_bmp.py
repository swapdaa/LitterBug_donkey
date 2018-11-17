# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# L3GD20
# This code is designed to work with the L3GD20_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

import smbus2 as smbus
import sqlite3
from datetime import datetime
import Adafruit_BMP.BMP085 as BMP085
import time

# Get I2C bus
bus = smbus.SMBus(1)

# Start BMP 
bmp = BMP085.BMP085()

# Connect to table
conn = sqlite3.connect("/home/pi/sensors", timeout=30000)
c = conn.cursor()


def get_gyro():
    t = str(datetime.now())
    bus.write_byte_data(0x40, 0x20, 0x0F)
    bus.write_byte_data(0x40, 0x23, 0x30)

    time.sleep(0.5)

    data0 = bus.read_byte_data(0x40, 0x28)
    data1 = bus.read_byte_data(0x40, 0x29)

    # Convert the data
    xGyro = data1 * 256 + data0
    if xGyro > 32767 :
        xGyro -= 65536

    data0 = bus.read_byte_data(0x40, 0x2A)
    data1 = bus.read_byte_data(0x40, 0x2B)

    # Convert the data
    yGyro = data1 * 256 + data0
    if yGyro > 32767 :
        yGyro -= 65536

    data0 = bus.read_byte_data(0x40, 0x2C)
    data1 = bus.read_byte_data(0x40, 0x2D)

    # Convert the data
    zGyro = data1 * 256 + data0
    if zGyro > 32767 :
        zGyro -= 65536
    #print("Rotation in X-Axis : %d" %xGyro)
    #print("Rotation in Y-Axis : %d" %yGyro)
    #print("Rotation in Z-Axis : %d" %zGyro)
    c.execute('''INSERT INTO gyro(date, x, y, z)
                              VALUES(?,?,?,?)''', (t,xGyro, yGyro, zGyro))
    conn.commit()
    #return xGyro, yGyro, zGyro
    return


def get_accel():
    t = str(datetime.now())
    bus.write_byte_data(0x68, 0x20, 0x27)
    bus.write_byte_data(0x68, 0x23, 0x00)

    time.sleep(0.5)

    data0 = bus.read_byte_data(0x68, 0x28)
    data1 = bus.read_byte_data(0x68, 0x29)

    # Convert the data
    xAccl = data1 * 256 + data0
    if xAccl > 32767 :
        xAccl -= 65536

    data0 = bus.read_byte_data(0x68, 0x2A)
    data1 = bus.read_byte_data(0x68, 0x2B)

    # Convert the data
    yAccl = data1 * 256 + data0
    if yAccl > 32767 :
        yAccl -= 65536

    data0 = bus.read_byte_data(0x68, 0x2C)
    data1 = bus.read_byte_data(0x68, 0x2D)

    # Convert the data
    zAccl = data1 * 256 + data0
    if zAccl > 32767 :
        zAccl -= 65536
    #print("Acceleration in X-Axis : %d" % xAccl)
    #print("Acceleration in Y-Axis : %d" % yAccl)
    #print("Acceleration in Z-Axis : %d" % zAccl)
    c.execute('''INSERT INTO accel(date, x, y, z)
                              VALUES(?,?,?,?)''', (t,xAccl, yAccl, zAccl))
    conn.commit()
    #return xAccl, yAccl, zAccl 
    return

def get_bmp():
    t = str(datetime.now())
    temp = bmp.read_temperature()
    pressure = bmp.read_pressure()
    alt = bmp.read_altitude()
    c.execute('''INSERT INTO bmp(date, temp, pressure, alt)
                              VALUES(?,?,?,?)''', (t,temp, pressure, alt))
    conn.commit()
    return

if __name__ == "__main__":
    get_gyro()
    get_accel()
    get_bmp()
    c.close()
