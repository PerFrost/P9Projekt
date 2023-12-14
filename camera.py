import cv2
from singleton import Singleton
from settings import Settings
class Camera(Singleton):
    def __init__(self, path = 0):
        self.cap = cv2.VideoCapture(path)

    def __del__(self):
        self.cap.release()

    def change_camera(self, path):
        self.cap.release()
        self.cap = cv2.VideoCapture(path)
        return self

    def change_resolution(self, width, height):
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        return self

    def getFrame(self):
        if not self.cap.isOpened():
            raise Exception("Camera could not be opened")

        try:
            success, frame = self.cap.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False
            return frame

        except Exception as e:
            print(e)
            pass

    @staticmethod
    def getCameraIndexes(indexRange = 5):
        indexList = []
        for i in range(0, indexRange):
            try:
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    indexList.append(i)
                    cap.release()
            except:
                pass
        return indexList
