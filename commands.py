import pyautogui
from settings import Settings

class Commands:
    def __init__(self):
        self.settings = Settings()

    def move_laser_pointer(self, landmarks):
        print(landmarks)
        try:
            x, y = landmarks
            pyautogui.moveTo(self.settings.monitor.x + (self.settings.monitor.width - x), self.settings.monitor.y + y)
            print("Pointing")

        except:
            print("hand outside screen")

    def toggle_laser_pointer(self):
        pyautogui.hotkey('ctrl', 'l')

    def next_slide(self):
        pyautogui.press('right')
        print("right")

    def prev_slide(self):
        pyautogui.press('left')
        print("left")

    def scroll_up(self):
        pyautogui.scroll(200)

    def scroll_down(self):
        pyautogui.scroll(-200)