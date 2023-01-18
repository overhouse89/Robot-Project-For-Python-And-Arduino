
# Import
import tkinter  # Tkinter

# Modules
from modules import robot_body
from modules import robot_serial_connection

# Tkinter
tk_head = tkinter.Tk()  # Screen

# Graphic
tk_head.geometry("400x200")  # Screen's size
tk_head.title("Dancing Robot")  # Screen's title

if robot_serial_connection.serial_arduino != "Connected":
	button_for_head = tkinter.Button(
		tk_head, 
		text = robot_body.head_button_text,
		width=15, 
		command= robot_body.body_head
	)
	button_for_head.pack()  # Pack
else:
	print("Arduino is not connected.")

# Loop
tk_head.mainloop()  # Screen is showing
