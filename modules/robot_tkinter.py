
# Imports
import tkinter  # Tkinter
import time

# Modules
from modules import robot_body
from modules import robot_serial_connection

# Tkinter
tk_screen = tkinter.Tk()  # Screen

# Graphic
tk_screen.geometry("400x200")  # Screen's size
tk_screen.title("Dancing Robot")  # Screen's title

if robot_serial_connection.serial_arduino == "Connected":
	# Button for robot's head
	button_for_head = tkinter.Button(
		tk_screen, 
		text = robot_body.robot_body_class.head_button_text,
		width=15, 
		command= robot_body.body_head
	)
	button_for_head.pack()  # Pack
else:
	print("Arduino is not connected.")

# Loop
tk_screen.mainloop()  # Screen is showing
