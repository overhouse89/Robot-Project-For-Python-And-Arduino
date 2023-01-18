
# Texts
head_button_text = "Head"

# Bools
button_head_off = True

# Class for robot's body
class robot_body_class():
    def __init__(self, body_name):
        self.body_name = body_name

# Robot's head
def body_head():
	global button_head_off

	if button_head_off:
		button_head_off = False
		print("Off")
	else:
		button_head_off = True
		print("On")