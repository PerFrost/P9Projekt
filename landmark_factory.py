import pyautogui

class LandmarkFactory:
    def __init__(self, landmark_data, settings):
        self.name, self.landmarks = landmark_data
        self.screen_size = pyautogui.size()
        self.set = settings

    def create_landmarks(self):
        if self.name == "mediapipe":

            if self.landmarks:
                self.landmarks = self.landmarks[0]

            self.landmarks = [[self.screen_size.width - (landmark.x * self.screen_size.width),
                               landmark.y * self.screen_size.height] for landmark in self.landmarks]

            print(self.landmarks)

        elif self.name == "mmpose":
            cameraYRes, cameraXRes = self.set.getCameraRes()

            self.landmarks = [[(landmark[0] / cameraXRes) * self.screen_size.width,
                               (landmark[1] / cameraYRes) * self.screen_size.height] for landmark in self.landmarks]

        return self.landmarks

