import pyautogui
from settings import Settings

class LandmarkFactory:
    def __init__(self):
        self.screen_size = pyautogui.size()
        self.set = Settings()

    def create_landmarks_for_screen_res(self, landmark_data):
        if self.set.model == "MediaPipe":
            landmark_data = [[self.set.monitor.width - (landmark.x * self.set.monitor.width),
                              landmark.y * self.set.monitor.height] for landmark in landmark_data]

        elif self.set.model == "MMPose" or self.set.model == "MMPose2":
            cam_res_x, cam_res_y = self.set.getCameraRes()

            landmark_data = [[self.set.monitor.width - (landmark[0] / cam_res_x) * self.set.monitor.width,
                              (landmark[1] / cam_res_y) * self.set.monitor.height] for landmark in landmark_data]

        return landmark_data

    def create_landmarks_for_screen_norm(self, landmark_data):
        if landmark_data:
            if self.set.model == "MediaPipe":
                cam_res_x, cam_res_y = self.set.getCameraRes()
                landmark_data = [[landmark.x * cam_res_x,
                                  landmark.y * cam_res_y] for landmark in landmark_data]

            elif self.set.model == "MMPose" or self.set.model == "MMPose2":
                landmark_data = [[landmark[0], landmark[1]] for landmark in landmark_data]

            base_x, base_y = landmark_data[0]

            landmark_data = [[landmark[0] - base_x, landmark[1] - base_y] for landmark in landmark_data]
            landmark_data = [x for xs in landmark_data for x in xs]

            max_value = max([abs(x) for x in landmark_data])

            landmark_data = [x / max_value for x in landmark_data]

        return landmark_data

    def create_landmarks_for_camera_res(self, landmark_data):
        if self.set.model == "MediaPipe":
            cam_res_x, cam_res_y = self.set.getCameraRes()
            landmark_data = [[landmark.x * cam_res_x, landmark.y * cam_res_y] for landmark in landmark_data]

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


