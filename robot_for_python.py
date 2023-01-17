
# Variables
serial_arduino = ""
disconnected_bool = True

# Imports
import serial  # Python will be connected to Arduino's Bluetooth
import time  # Waiting

# Module
from modules import robot_tkinter  # Tkinter for robot's head

try:
	serial_connection = serial.Serial("/dev/cu.HC-06")  # Bluetooth is connected
	time.sleep(2)  # Waiting for next line
	serial_arduino = "Connected"
except Exception:
	while disconnected_bool:
		time.sleep(2)  # Waiting for next line
		serial_arduino = "Disconnected"
		disconnected_bool = False

robot_tkinter.tkinter_head(serial_arduino)  # Tkinter
