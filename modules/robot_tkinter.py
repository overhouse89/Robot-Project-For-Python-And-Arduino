
# Tkinter
import tkinter

# Module
from modules import robot_body  # Class for robot's body

def robot_serial_connected():
    print("Connected")

def tkinter_head(serial_name):
    # Tkinter
    tk_head = tkinter.Tk()  # Screen

    # Graphic
    tk_head.geometry("800x600")  # Screen's size
    tk_head.title("Dancing Robot")  # Screen's title

    # Python's code is searching serial's address
    if serial_name == "Disconnected":  # Serial's address is not found
        print("Arduino is not connected.")
        button_for_disconnected = tkinter.Button(
            tk_head,
            text ="Connect",
            width=15,
            command=robot_serial_connected
        )

        button_for_disconnected.pack()
    else:  # Serial's address is found

        # Buttons
        button_for_head = tkinter.Button(
            tk_head, 
            text ="Head", 
            width=15, 
            command=robot_body.body_head
        )

        button_for_left_arm = tkinter.Button(
            tk_head,
            text ="Left Arm", 
            width=15, 
            command=robot_body.body_left_arm
        )

        button_for_right_arm = tkinter.Button(
            tk_head, 
            text ="Right Arm", 
            width=15, 
            command=robot_body.body_right_arm
        )

        # Packs
        button_for_head.pack()
        button_for_left_arm.pack()
        button_for_right_arm.pack()

    # Loop
    tk_head.mainloop()  # Screen is showing
