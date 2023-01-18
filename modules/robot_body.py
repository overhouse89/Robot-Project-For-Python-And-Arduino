
# Bools
head_button_text = "Head"

# Class for robot's body
class robot_body_class():
    def __init__(self, body_name):
        self.body_name = body_name

# Robot's head
def body_head():
	body_name_head = robot_body_class("Head")
	print(body_name_head.body_name)
