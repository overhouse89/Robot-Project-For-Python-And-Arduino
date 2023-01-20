
# Imports
import tkinter  # Tkinter

# Modules
from modules import robot_body
from modules import robot_serial_connection

# Tkinter
tk_screen = tkinter.Tk()  # Screen

# Graphic
tk_screen.geometry("600x400")  # Screen's size
tk_screen.title("Dancing Robot")  # Screen's title

if robot_serial_connection.serial_arduino == "Connected":
	# Button for robot's head
	button_for_head = tkinter.Button(
		tk_screen, 
		text = "Head",
		width=15,
		command= robot_body.body_head
	)
	button_for_head.place(x=220, y=50)  # Position

	# Button for robot's left arm
	button_for_left_arm = tkinter.Button(
		tk_screen, 
		text = "Left Arm",
		width=15,
		command= robot_body.body_left_arm
	)
	button_for_left_arm.place(x=50, y=150)  # Position

	# Button for robot's right arm
	button_for_right_arm = tkinter.Button(
		tk_screen, 
		text = "Right Arm",
		width=15,
		command= robot_body.body_right_arm
	)
	button_for_right_arm.place(x=390, y=150)  # Position
else:
	print("Arduino is not connected.")

# Loop
tk_screen.mainloop()  # Screen is showing
