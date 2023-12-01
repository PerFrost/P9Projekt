import cv2

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

class Camera(Singleton):
    def __init__(self, path = 0):
        self.cap = cv2.VideoCapture(path)

    def __del__(self):
        self.cap.release()

    def getFrame(self):
        if not self.cap.isOpened():
            raise Exception("Camera could not be opened")

        try:
            success, frame = self.cap.read()
            return frame

        except Exception as e:
            print(e)
            pass

    @staticmethod
    def getCameraIndexes(indexRange = 5):
        indexList = []
        for i in range(0, indexRange):
            try:
                cap = cv2.VideoCapture(indexList)
                if cap:
                    indexList.append(i)
            except:
                pass
        return indexList