import Adafruit_GPIO.SPI as SPI
import io
import serial
import ST7735
import gpiozero

from PIL import ImageFont

# TFT display parameters
TFT_WIDTH = 128
TFT_HEIGHT = 128
TFT_SPEED_HZ = 15000000

# RPi GPIO & SPI configuration for TFT display
TFT_RS = 24
TFT_RST = 25
TFT_SPI_PORT = 0
TFT_SPI_DEVICE = 0


def nmea_checksum(message):
    # calculate a simple XOR checksum and return the value as a hex string
    checksum = 0
    for char in message:
        checksum = checksum ^ ord(char)
    return "%X" % checksum


def open_serial_reader(port):
    # open the serial port in buffered, non-blocking mode at the GPS's default baud rate
    com_port = serial.Serial(port, 9600, timeout=1)
    return io.BufferedReader(com_port)


def create_display():
    # Create TFT LCD display driver
    disp = ST7735.ST7735(
        TFT_RS,
        rst=TFT_RST,
        spi=SPI.SpiDev(
            TFT_SPI_PORT,
            TFT_SPI_DEVICE,
            max_speed_hz=TFT_SPEED_HZ),
        width=TFT_WIDTH,
        height=TFT_HEIGHT)

    # Initialize display, clear the buffer to white, write buffer to screen
    disp.begin()
    disp.clear((0, 0, 0))
    disp.display()

    return disp


led = gpiozero.LED(4)

serial_data = open_serial_reader("/dev/serial0")
tft_display = create_display()

draw = tft_display.draw()

small_font = ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 8)
medium_font = ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 16)
big_font = ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 32)

for line in serial_data:
    if line.startswith("$GPGGA"):
        msg, msg_checksum = line.lstrip("$").rstrip().split("*")
        calc_checksum = nmea_checksum(msg)
        if msg_checksum != calc_checksum:
            print "ERROR! Calc. checksum: " + calc_checksum + " did not match received checksum " + msg_checksum + "!"
        else:
            elements = msg.split(",")
            if len(elements) != 15:
                print "GPGGA received message does not contain the expected data elements!"
            else:
                if elements[6] != "1":
                    print "No valid GPS signal"
                else:
                    led.on()
                    time = "TME " + elements[1]
                    latitude = "LAT " + elements[2] + " " + elements[3]
                    longitude = "LON " + elements[4] + " " + elements[5]
                    altitude = "ALT " + elements[9]

                    draw.rectangle((0, 0, TFT_WIDTH, TFT_HEIGHT), fill=0, outline=0)
                    draw.text((5, 10), time, font=medium_font, fill=(255, 255, 255))
                    draw.text((5, 25), latitude, font=medium_font, fill=(255, 0, 0))
                    draw.text((5, 40), longitude, font=medium_font, fill=(0, 255, 0))
                    draw.text((5, 55), altitude, font=medium_font, fill=(0, 0, 255))
                    tft_display.display()
                    led.off()
