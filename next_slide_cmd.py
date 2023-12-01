from gesture_command import GestureCommand

class NextSlideCmd(GestureCommand):
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.next_slide()