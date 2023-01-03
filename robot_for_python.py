
# Robot for Python

import serial
import time

try:
	print("Arduino is connected.")
	arduino_connection = serial.Serial("/dev/cu.usbserial-1420", 9600)
	arduino_connection.close()
except Exception:
	print("Arduino is not connected.")

