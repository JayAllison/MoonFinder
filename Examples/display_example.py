# using display driver from: https://github.com/cskau/Python_ST7735
# dependencies: sudo apt-get install build-essential python-dev python-smbus python-pip python-imaging python-numpy
# for me, only python-imaging was not already installed

# I got the cheap Amazon display I purchased working with the examples using this pinout:
#   * 5V - any RPi 5V
#   * GND - any RPi GND
#   * GND -NC
#   * NC - NC
#   * NC -NC
#   * LED - I connected this to RPi 3.3V
#   * SCL - RPi SCLK
#   * SDA - RPi MOSI
#   * RS - GPIO 24 (per the example)
#   * RST - GPIO 25 (per the example)
#   * CS - RPi CE0
# The examples are written for a 160x128 display, this one is 128x128

# from PIL import Image
# from PIL import ImageDraw
from PIL import ImageFont

# need to install this from source: https://github.com/cskau/Python_ST7735
import ST7735
# import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

# TFT display parameters
TFT_WIDTH = 128
TFT_HEIGHT = 128
#SPEED_HZ = 4000000
# TODO: try a faster speed and see how well it works
SPEED_HZ = 15000000

# RPi GPIO & SPI configuration for TFT display
RS = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0

# Create TFT LCD display driver
disp = ST7735.ST7735(
    RS,
    rst=RST,
    spi=SPI.SpiDev(
        SPI_PORT,
        SPI_DEVICE,
        max_speed_hz=SPEED_HZ),
    width=TFT_WIDTH,
    height=TFT_HEIGHT)

# Initialize display, clear the buffer to white, write buffer to screen
disp.begin()
disp.clear((0, 0, 0))
disp.display()
draw = disp.draw()

text = "Hello, World!"
# font = ImageFont.load_default()
small_font = ImageFont.truetype("../Fonts/Perfect DOS VGA 437 Win.ttf", 8)
medium_font = ImageFont.truetype("../Fonts/Perfect DOS VGA 437 Win.ttf", 16)
big_font = ImageFont.truetype("../Fonts/Perfect DOS VGA 437 Win.ttf", 32)
draw.text((10, 10), text, font=small_font, fill=(255, 0, 0))
draw.text((10, 30), text, font=medium_font, fill=(0, 255, 0))
draw.text((10, 60), text, font=big_font, fill=(0, 0, 255))

disp.display()
