
# Imports
import serial  # Serial's address
import time  # Waiting

# Insert
appendBody = ["Head","Left Arm","Right Arm","All bodies"]

# String
appendText = ""

class robot_body_class:
    def __init__(self, body_name):
        self.body_name = body_name

def send_data_to_arduino():
    # Classes
    head_class = robot_body_class("Head")
    left_arm_class = robot_body_class("Left Arm")
    right_arm_class = robot_body_class("Right Arm")
    all_bodies_class = robot_body_class("All bodies")

    # Serial
    serial_connection = serial.Serial("/dev/rfcomm0")  # Bluetooth is connected
    
    # One body is turning
    if appendBody[0] == appendText:
        time.sleep(0.1)
        serial_connection.write(b'H')  # H = Head
    elif appendBody[1] == appendText:
        serial_connection.write(b'LA')  # LA = Left arm
    elif appendBody[2] == appendText:
        time.sleep(0.1)
        serial_connection.write(b'RA')  # RA = Right arm
    elif appendBody[3] == appendText:
        time.sleep(0.1)
        serial_connection.write(b'ALLB')  # ALLB = ALL BODIES
