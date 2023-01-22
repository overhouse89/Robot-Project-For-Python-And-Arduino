
# Imports
import serial  # Serial's address
import time  # Waiting

# buttons for loop
def while_buttons(button_name):
    serial_connection = serial.Serial("/dev/rfcomm0")  # Bluetooth is connected
    #serial_connection = serial.Serial("/dev/ttyUSB0")
    if button_name == "Head":
        while True:
            time.sleep(0.5)
            serial_connection.write(b'Head')
            time.sleep(6.8)
            serial_connection.write(b'No Head')
            print("OK")
            break

# Robot's head
def body_head():
    while_buttons("Head")

# Robot's left arm
def body_left_arm():
    print("Left Arm")
    #while_buttons("Left Arm")

# Robot's right arm
def body_right_arm():
    print("Right Arm")
    #while_buttons("Right Arm")
