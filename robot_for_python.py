
# Imports
import serial
import time

# Modules
from modules import robot_body  # All robot's body
from modules import robot_tkinter  # Tkinter for robot's head

try:
	serial_connection = serial.Serial("/dev/cu.HC-06")  # Bluetooth is connected
except Exception:
	print("Arduino isn't connected.")  # Disconnected

robot_tkinter.tkinter_head()  # Tkinter
