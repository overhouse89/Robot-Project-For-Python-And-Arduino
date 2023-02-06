
from modules.robot_tkinter import *

def tk_body_active_button():
	# Color for head
	button_for_head["bg"] = 'black'
	button_for_head["fg"] = 'white'
	button_for_head["activebackground"] = 'black'
	button_for_head["activeforeground"] = 'white'
	button_for_head["state"] = ACTIVE

	# Color for left arm
	button_for_left_arm["bg"] = 'black'
	button_for_left_arm["fg"] = 'white'
	button_for_left_arm["activebackground"] = 'black'
	button_for_left_arm["activeforeground"] = 'white'
	button_for_left_arm["state"] = ACTIVE

	# Color for right arm
	button_for_right_arm["bg"] = 'black'
	button_for_right_arm["fg"] = 'white'
	button_for_right_arm["activebackground"] = 'black'
	button_for_right_arm["activeforeground"] = 'white'
	button_for_right_arm["state"] = ACTIVE

	# Color for all bodies
	button_for_all_bodies["bg"] = '#461257'
	button_for_all_bodies["fg"] = 'white'
	button_for_all_bodies["activebackground"] = '#461257'
	button_for_all_bodies["activeforeground"] = 'white'
	button_for_all_bodies["state"] = ACTIVE

# Disable for button
def tk_body_disable_button():
	button_for_head["state"] = DISABLED
	button_for_left_arm["state"] = DISABLED
	button_for_right_arm["state"] = DISABLED
	button_for_all_bodies["state"] = DISABLED

# Send data to robot_body.py
def body_waiting():
	if robot_body.appendText == "Head":
		tk_body_active_button()
		button_for_head["text"] = "Head"
		robot_body.appendText = ""
	elif robot_body.appendText == "Left Arm":
		tk_body_active_button()
		button_for_left_arm["text"] = "Left Arm"
		robot_body.appendText = ""
	elif robot_body.appendText == "Right Arm":
		tk_body_active_button()
		button_for_right_arm["text"] = "Right Arm"
		robot_body.appendText = ""
	elif robot_body.appendText == "All bodies":
		tk_body_active_button()
		button_for_all_bodies["text"] = "ALL"
		robot_body.appendText = ""

# Robot's head
def body_head_insert():
	tk_body_disable_button()
	button_for_head["text"] = "Turning.."
	robot_body.appendText = "Head"
	robot_body.send_data_to_arduino()
	tk_screen.after(5200, body_waiting)

# Robot's left arm
def body_left_arm_insert():
	tk_body_disable_button()
	button_for_left_arm["text"] = "Turning.."
	robot_body.appendText = "Left Arm"
	robot_body.send_data_to_arduino()
	tk_screen.after(5400, body_waiting)

# Robot's right arm
def body_right_arm_insert():
	tk_body_disable_button()
	button_for_right_arm["text"] = "Turning.."
	robot_body.appendText = "Right Arm"
	robot_body.send_data_to_arduino()
	tk_screen.after(5400, body_waiting)

# All robot's bodies
def body_all_insert():
	tk_body_disable_button()
	button_for_all_bodies["text"] = "Turning.."
	robot_body.appendText = "All bodies"
	robot_body.send_data_to_arduino()
	tk_screen.after(14000, body_waiting)

# Active for button
def tk_body_active_button():
	# Color for head
	button_for_head["bg"] = 'black'
	button_for_head["fg"] = 'white'
	button_for_head["activebackground"] = 'black'
	button_for_head["activeforeground"] = 'white'
	button_for_head["state"] = ACTIVE

	# Color for left arm
	button_for_left_arm["bg"] = 'black'
	button_for_left_arm["fg"] = 'white'
	button_for_left_arm["activebackground"] = 'black'
	button_for_left_arm["activeforeground"] = 'white'
	button_for_left_arm["state"] = ACTIVE

	# Color for right arm
	button_for_right_arm["bg"] = 'black'
	button_for_right_arm["fg"] = 'white'
	button_for_right_arm["activebackground"] = 'black'
	button_for_right_arm["activeforeground"] = 'white'
	button_for_right_arm["state"] = ACTIVE

	# Color for all bodies
	button_for_all_bodies["bg"] = '#461257'
	button_for_all_bodies["fg"] = 'white'
	button_for_all_bodies["activebackground"] = '#461257'
	button_for_all_bodies["activeforeground"] = 'white'
	button_for_all_bodies["state"] = ACTIVE

# Disable for button
def tk_body_disable_button():
	button_for_head["state"] = DISABLED
	button_for_left_arm["state"] = DISABLED
	button_for_right_arm["state"] = DISABLED
	button_for_all_bodies["state"] = DISABLED

# Send data to robot_body.py
def body_waiting():
	if robot_body.appendText == "Head":
		tk_body_active_button()
		button_for_head["text"] = "Head"
		robot_body.appendText = ""
	elif robot_body.appendText == "Left Arm":
		tk_body_active_button()
		button_for_left_arm["text"] = "Left Arm"
		robot_body.appendText = ""
	elif robot_body.appendText == "Right Arm":
		tk_body_active_button()
		button_for_right_arm["text"] = "Right Arm"
		robot_body.appendText = ""
	elif robot_body.appendText == "All bodies":
		tk_body_active_button()
		button_for_all_bodies["text"] = "ALL"
		robot_body.appendText = ""

# Robot's head
def body_head_insert():
	tk_body_disable_button()
	button_for_head["text"] = "Turning.."
	robot_body.appendText = "Head"
	robot_body.send_data_to_arduino()
	tk_screen.after(5200, body_waiting)

# Robot's left arm
def body_left_arm_insert():
	tk_body_disable_button()
	button_for_left_arm["text"] = "Turning.."
	robot_body.appendText = "Left Arm"
	robot_body.send_data_to_arduino()
	tk_screen.after(5400, body_waiting)

# Robot's right arm
def body_right_arm_insert():
	tk_body_disable_button()
	button_for_right_arm["text"] = "Turning.."
	robot_body.appendText = "Right Arm"
	robot_body.send_data_to_arduino()
	tk_screen.after(5400, body_waiting)

# All robot's bodies
def body_all_insert():
	tk_body_disable_button()
	button_for_all_bodies["text"] = "Turning.."
	robot_body.appendText = "All bodies"
	robot_body.send_data_to_arduino()
	tk_screen.after(14000, body_waiting)

