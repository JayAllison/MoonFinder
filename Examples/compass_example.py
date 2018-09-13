# derived from https://github.com/adafruit/Adafruit_Python_LSM303/blob/master/examples/simpletest.py

import math
import time

# sudo pip install adafruit-lsm303
import Adafruit_LSM303

# device is connected on I2C Bus 0
lsm303 = Adafruit_LSM303.LSM303()

while True:
    accelerometer, magnetometer = lsm303.read()
    # this is how the internet says to turn magnetometer X & Y into a compass heading...
    # Yes, the reading back from this compass library is (X, Z, Y) - that's not a typo!
    # for this example, I'm using a 180-degree offset because I want :
    #   N = 0 (or 360)
    #   E = 90
    #   S = 180
    #   W = 270
    compass_heading = math.atan2(magnetometer[2], magnetometer[0]) * 180 / math.pi + 180
    print "Compass heading for " + str(magnetometer) + ": " + str(compass_heading)
    time.sleep(0.5)
