from gps3 import gps3
from datetime import datetime
import sqlite3
import time


gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

conn = sqlite3.connect("/home/pi/sensors", timeout=30000)
c = conn.cursor()


i = 0
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        #print('Altitude = ', data_stream.TPV['alt'])
        #print('Latitude = ', data_stream.TPV['lat'])
        #print('Longitude = ', data_stream.TPV['lon'])
        time.sleep(0.5)
        i += 1
    if i == 10:
        t = str(datetime.now())
        alt = data_stream.TPV['alt']
        lat = data_stream.TPV['lat']
        lon = data_stream.TPV['lon']
        c.execute('''INSERT INTO gps(date, alt, lat, lon)
                                 VALUES(?,?,?,?)''', (t, alt, lat, lon))
        conn.commit()
        break
c.close()


