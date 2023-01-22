
# Imports
import serial  # Serial's address
import time  # Waiting

# Variables
serial_arduino = ""

#Python's code is searching serial's address
try:
	# Serial's address is connected
	#serial_connection = serial.Serial("/dev/ttyUSB0")  # USB is connected  For Raspberry Pi
	serial_connection = serial.Serial("/dev/rfcomm0")  # Bluetooth is connected  For Raspberry Pi
	# Write line  --->   sudo rfcomm connect 0 98:D3:31:F7:61:83  ---->  for Raspberry Pi's terminal
	serial_arduino = "Connected"
	print("connected")
	time.sleep(2)
	serial_connection.write(b'No Head')
	serial_connection.close()
except Exception:
	# Serial's address is not connected
	time.sleep(2)  # Waiting for next line
	serial_arduino = "Disconnected"
	print("Disconnected")
	
