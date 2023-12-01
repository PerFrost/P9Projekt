class GestureRecognizer:

    def __init__(self, command):
        self.command = command

    def recognize_gesture(self, frame):
        self.command.execute(frame)