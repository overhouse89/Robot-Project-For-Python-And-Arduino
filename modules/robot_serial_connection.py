
# Imports
import serial  # Serial's address
import time  # Waiting

# Variables
serial_arduino = ""

# Python's code is searching serial's address
while True:
	try:
		# Serial's address is connected
		serial_connection = serial.Serial("/dev/rfcomm0")  # Bluetooth is connected
		serial_arduino = "Connected"
		time.sleep(2)
		serial_connection.close()
		break
	except Exception:
		# Serial's address is not connected
		time.sleep(2)  # Waiting for next line
		serial_arduino = "Disconnected"
		break
	
