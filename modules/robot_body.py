
# Bools
button_head_off = True
button_left_off = True
button_right_off = True

# Robot's head
def body_head():
    print("Head")
    global button_head_off
    if button_head_off:
        button_head_off = False
    else:
        button_head_off = True

# Robot's left arm
def body_left_arm():
    print("Left Arm")
    global button_left_off
    if button_left_off:
        button_left_off = False
    else:
        button_left_off = True

# Robot's right arm
def body_right_arm():
    print("Right Arm")
    global button_right_off
    if button_right_off:
        button_right_off = False
    else:
        button_right_off = True
