
# Imports
import serial  # Python will be connected to Arduino's Bluetooth
import time  # Waiting

# Variables
serial_arduino = ""

# Python's code is searching serial's address
try:
    # Serial's address is connected
	serial_connection = serial.Serial("/dev/cu.HC-06")  # Bluetooth is connected
	time.sleep(2)  # Waiting for next line
	serial_arduino = "Connected"
	serial_connection.close()
except Exception:
    # Serial's address is not connected
	time.sleep(2)  # Waiting for next line
	serial_arduino = "Disconnected"