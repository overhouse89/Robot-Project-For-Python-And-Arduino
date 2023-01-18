
# Imports
from modules import robot_serial_connection

# Bools
button_head_off = True

# Class for robot's body
class robot_body_class():
    head_button_text = "Head"
    left_arm_button_text = "Left Arm"
    right_arm_button_text = "Right Arm"

# Robot's head
def body_head():
    global button_head_off
    if button_head_off:
        button_head_off = False
    else:
        button_head_off = True
