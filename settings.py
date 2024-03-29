import screeninfo
from singleton import Singleton

class Settings(Singleton):
    def setDefault(self):
        self.camera_index = -1
        self.calibration_points = {}
        self.camera_resolution = "640x480"
        self.monitor = str(screeninfo.get_monitors()[0])
        self.model = "MediaPipe"

        return self


    def setSettings(self, camera_index, calibration_points, camera_resolution, monitor, model):
        self.camera_index = camera_index
        self.calibration_points = calibration_points
        self.camera_resolution = camera_resolution
        self.monitor = monitor
        self.model = model

        return self

    def getCameraRes(self):
        return [int(x) for x in self.camera_resolution.split("x")]
