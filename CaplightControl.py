# -*-coding:Utf-8 -*

import serial
import sys

caplight = serial.Serial('COM7', 9600)
print caplight
print "message", caplight.readline()
caplight.write(sys.argv[1])
caplight.close()