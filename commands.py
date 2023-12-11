import pyautogui

class Commands:
    def __init__(self, settings):
        self.settings = settings

    def move_laser_pointer(self, landmarks):
        try:
            x, y = landmarks
            pyautogui.moveTo(self.settings.monitor.x + x, self.settings.monitor.y + y)

        except:
            print("hand outside screen")

    def next_slide(self):
        pyautogui.press('right')

    def prev_slide(self):
        pyautogui.press('left')

    def scroll_up(self):
        pyautogui.scroll(200)

    def scroll_down(self):
        pyautogui.scroll(-200)