import pyautogui

class LandmarkFactory:
    def __init__(self, settings):
        self.screen_size = pyautogui.size()
        self.set = settings

    def create_landmarks_for_screen_res(self, landmark_data):
        if self.set.model == "MediaPipe":
            landmark_data = [[self.set.monitor.width - (landmark.x * self.set.monitor.width),
                               landmark.y * self.set.monitor.height] for landmark in landmark_data]

        elif self.set.model == "MMPose" or self.set.model == "MMPose2":
            cameraXRes, cameraYRes = self.set.getCameraRes()

            landmark_data = [[self.set.monitor.width - (landmark[0] / cameraXRes) * self.set.monitor.width,
                               (landmark[1] / cameraYRes) * self.set.monitor.height] for landmark in landmark_data]

        return landmark_data

    def create_landmarks_for_camera_res(self, landmark_data):
        if self.set.model == "MediaPipe":
            cameraXRes, cameraYRes = self.set.getCameraRes()
            landmark_data = [[landmark.x * cameraXRes, landmark.y * cameraYRes] for landmark in landmark_data]

        elif self.set.model == "MMPose" or self.set.model == "MMPose2":
            landmark_data = [[landmark[0], landmark[1]] for landmark in landmark_data]

        return landmark_data

    def create_landmarks_for_calibration(self, landmarks):
        cam = self.create_landmarks_for_camera_res(landmarks)

        if cam and len(cam) > 8:
            tip_of_index_finger_cam = cam[8]

            x_cam = tip_of_index_finger_cam[0]
            y_cam = tip_of_index_finger_cam[1]

            try:
                if self.set.calibration_points["x_min"] <= x_cam <= self.set.calibration_points["x_max"] and \
                   self.set.calibration_points["y_min"] <= y_cam <= self.set.calibration_points["y_max"]:
                    x_normal = (x_cam - self.set.calibration_points["x_min"]) / (self.set.calibration_points["x_max"] - self.set.calibration_points["x_min"])
                    y_normal = (y_cam - self.set.calibration_points["y_min"]) / (self.set.calibration_points["y_max"] - self.set.calibration_points["y_min"])

                    return [x_normal * self.set.monitor.width, y_normal * self.set.monitor.height]
            except:
                return []


