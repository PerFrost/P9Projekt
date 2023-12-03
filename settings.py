import cv2
class Settings:

    def __init__(self):
        self.cameraList = []
        self.calibrationPoints = []
        self.cameraResolution = (480, 640)

    def getCameraRes(self):
        return self.cameraResolution
