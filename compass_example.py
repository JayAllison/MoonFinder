# derived from https://github.com/adafruit/Adafruit_Python_LSM303/blob/master/examples/simpletest.py

import math
import time

# sudo pip install adafruit-lsm303
import Adafruit_LSM303

# device is connected on I2C Bus 0
lsm303 = Adafruit_LSM303.LSM303()

while True:
    accelerometer, magnetometer = lsm303.read()
    compass_heading = math.atan2(magnetometer[1], magnetometer[0]) * 180 / math.pi
    print "Compass heading for " + str(compass_heading) + ": " + str(compass_heading)
    time.sleep(0.5)
