import pyautogui

class Commands:
    def move_laser_pointer(self, x_coord, y_coord):
        try:
            pyautogui.moveTo(x_coord, y_coord)

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