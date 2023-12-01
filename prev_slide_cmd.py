from gesture_command import GestureCommand

class PrevSlideCmd(GestureCommand):
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.prev_slide()