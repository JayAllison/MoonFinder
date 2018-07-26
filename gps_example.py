import io
import serial


def nmea_checksum(message):
    checksum = 0
    for char in message:
        checksum = checksum ^ ord(char)

    return "%X" % checksum


# open the serial port in buffered, non-blocking mode at the GPS's default baud rate
com_port = serial.Serial("COM6", 9600, timeout=1)
serial_data = io.BufferedReader(com_port)

print "Listening for GPS NMEA data on " + com_port.name + " (" + str(com_port.is_open) + ")..."

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
                    print "Latitude: " + elements[2] + " " + elements[3] + ",",
                    print "Longitude: " + elements[4] + " " + elements[5] + ",",
                    print "Altitude: " + elements[9]
