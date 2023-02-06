
# Imports
from tkinter import *  # Tkinter

# Modules
from modules import robot_serial_connection
from modules.tkinter_for_button import *

# Tkinter
tk_screen = Tk()  # Screen

# Graphic
tk_screen.geometry("800x950")  # Screen's size
tk_screen.eval('tk::PlaceWindow . center')  # Screen on center
tk_screen.title("Dancing Robot")  # Screen's title

if robot_serial_connection.serial_arduino == "Connected":
	# Photo
	tk_image_for_buttons = PhotoImage(file="imgs/arduino_and_python_dancing_robot_bg_buttons.png")  # Image

	# Label for image
	tk_label_for_buttons = Label(
		tk_screen,
		image=tk_image_for_buttons
	).place(x=0, y=0)

	# Button for robot's head
	button_for_head = Button(
		tk_screen, 
		text = "Head",
		width=9, 
		height=2, 
		font=("Arial",18),
		bg='black',
		fg='white',
		activebackground="black",
		activeforeground="white",
		highlightbackground="white",
		highlightthickness=6,
		state=ACTIVE,
		command= body_head_insert
	)
	button_for_head.pack(side='top', pady=295) # Pack

	# Button for robot's left arm
	button_for_left_arm = Button(
		tk_screen, 
		text = "Left Arm",
		width=9, 
		height=2, 
		font=("Arial",18),
		bg='black',
		fg='white',
		activebackground="black",
		activeforeground="white",
		highlightbackground="white",
		highlightthickness=6,
		state=ACTIVE,
		command= body_left_arm_insert
	)
	button_for_left_arm.pack(side='left', padx=70) # Pack

	# Button for robot's right arm
	button_for_right_arm = Button(
		tk_screen, 
		text = "Right Arm",
		width=9, 
		height=2, 
		font=("Arial",18),
		bg='black',
		fg='white',
		activebackground="black",
		activeforeground="white",
		highlightbackground="white",
		highlightthickness=6,
		state=ACTIVE,
		command= body_right_arm_insert
	)
	button_for_right_arm.pack(side='right', padx=80) # Pack

	# Button for all robot's bodies
	button_for_all_bodies = Button(
		tk_screen, 
		text = "ALL",
		width=11, 
		height=1, 
		font=("Arial",18),
		bg='#461257',
		fg='white',
		activebackground="#461257",
		activeforeground="white",
		highlightbackground="#461257",
		highlightthickness=6,
		state=ACTIVE,
		command= body_all_insert
	)
	button_for_all_bodies.pack(side='bottom', pady=10) # Pack

else:
	# Photo
	tk_image = PhotoImage(file="imgs/arduino_is_not_connect.png")  # Image

	# Label for image
	tk_label = Label(
		tk_screen,
		image=tk_image
	).place(x=0, y=0)

	# Button for closing
	tk_disconnected_button = Button(
		tk_screen,
		text="Close", 
		width=11, 
		height=1, 
		font=("Arial",18),
		bg='#461257',
		fg='white',
		activebackground="#461257",
		activeforeground="white",
		highlightbackground="#461257",
		highlightthickness=6,
		state=ACTIVE,
		command=tk_screen.destroy
	)
	tk_disconnected_button.pack(side='bottom', pady=10) # Pack

# Loop
tk_screen.mainloop()  # Screen is showing
