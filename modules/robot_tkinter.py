
# Tkinter
import tkinter

def tkinter_head():
    # Tkinter
    tk_head = tkinter.Tk()  # Screen

    # Graphic
    tk_head.geometry("800x600")  # Screen's size
    tk_head.title("Dancing Robot")  # Screen's title

    # Buttons
    button_for_head = tkinter.Button(tk_head, text ="Head", width=15)  # Head button
    button_for_left_arm = tkinter.Button(tk_head, text ="Left Arm", width=15)  # Left arm button
    button_for_right_arm = tkinter.Button(tk_head, text ="Right Arm", width=15)  # Right arm button

    # Packs
    button_for_head.pack()
    button_for_left_arm.pack()
    button_for_right_arm.pack()

    # Loop
    tk_head.mainloop()  # Screen is showing
