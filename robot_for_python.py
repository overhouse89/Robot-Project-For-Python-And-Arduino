# Robot for Python

# Imports
import serial
import time

# Modules
import robot_body
import robot_tkinter

# Select serial's address
select_serial_input = input("Address: ").strip()
print("Waiting..")
time.sleep(2)

try:
	serial_connection = serial.Serial("/dev/cu.HC-06")  # Bluetooth is connected
	serial_connection.write(b's')
	serial_connection.write(b'k')
	while True:
		body_input = input("BODY: ").strip()  # Robot's body
		if body_input == 'a':
			serial_connection.write(b'a')  # Robot's head is turning left
		elif body_input == 's':
			serial_connection.write(b's')  # Robot's head is turning center
		elif body_input == 'd':
			serial_connection.write(b'd')  # Robot's head is turning right
except Exception:
	# Disconnected
	print(select_serial_input,"isn't connected.")


