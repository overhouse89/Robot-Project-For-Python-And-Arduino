
class robot_body_class():
    def __init__(self, body_name):
        self.body_name = body_name

# Robot's head
def body_head():
    body_name_head = robot_body_class("Head")
    print(body_name_head.body_name)

# Robot's left arm
def body_left_arm():
    body_name_left_arm = robot_body_class("Left Arm")
    print(body_name_left_arm.body_name)

# Robot's right arm
def body_right_arm():
    body_name_right_arm = robot_body_class("Right Arm")
    print(body_name_right_arm.body_name)
