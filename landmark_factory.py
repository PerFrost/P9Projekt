import pyautogui

class LandmarkFactory:
    def __init__(self, settings):
        self.screen_size = pyautogui.size()
        self.set = settings

    def create_landmarks(self, landmark_data):
        if self.set.model == "MediaPipe":
            landmark_data = [[self.screen_size.width - (landmark.x * self.screen_size.width),
                               landmark.y * self.screen_size.height] for landmark in landmark_data]

        elif self.set.model == "MMPose":
            cameraYRes, cameraXRes = self.set.getCameraRes()

            landmark_data = [[self.screen_size.width - (landmark[0] / cameraXRes) * self.screen_size.width,
                               (landmark[1] / cameraYRes) * self.screen_size.height] for landmark in landmark_data]

        return landmark_data

