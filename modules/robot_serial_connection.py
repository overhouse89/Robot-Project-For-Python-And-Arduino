
# Imports
import serial  # Serial's address
import time  # Waiting

# Modules
#from modules import robot_body

# Variables
serial_arduino = ""

# Python's code is searching serial's address
try:
    # Serial's address is connected
	serial_connection = serial.Serial("/dev/cu.usbserial-1410")  # Bluetooth is connected
	time.sleep(2)
	serial_connection.write(b'b')
	time.sleep(2)
	serial_connection.write(b'a')
	serial_arduino = "Connected"
	print("Connected")
	serial_connection.close()
except Exception:
    # Serial's address is not connected
	time.sleep(2)  # Waiting for next line
	serial_arduino = "Disconnected"
	