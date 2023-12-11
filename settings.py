import screeninfo


class Settings:
    def __init__(self):
        self.camera_index = -1
        self.calibration_points = {}
        self.camera_resolution = "640x480"
        self.monitor = str(screeninfo.get_monitors()[0])
        self.model = "MediaPipe"

    def __init__(self, camera_index, calibration_points, camera_resolution, monitor, model):
        self.camera_index = camera_index
        self.calibration_points = calibration_points
        self.camera_resolution = camera_resolution
        self.monitor = monitor
        self.model = model

    def getCameraRes(self):
        return [int(x) for x in self.camera_resolution.split("x")]
