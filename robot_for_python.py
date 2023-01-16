# Robot for Python

# Imports
import serial
import time

try:
	ser = serial.Serial("/dev/cu.HC-06")  # Bluetooth is connected
	ser.write(b's')
	ser.write(b'k')
	while True:
		test_input = input("BODY: ").strip()  # Robot's body
		if test_input == 'a':
			ser.write(b'a')  # Robot's head is turning left
		elif test_input == 's':
			ser.write(b's')  # Robot's head is turning center
		elif test_input == 'd':
			ser.write(b'd')  # Robot's head is turning right
except Exception:
	# Disconnected
	print("Arduino isn't connected.")


