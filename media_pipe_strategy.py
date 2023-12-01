import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import cv2
from model_strategy import ModelStrategy

class MediaPipeStrategy(ModelStrategy):

    def __init__(self):
        self.base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
        self.options = vision.HandLandmarkerOptions(base_options=self.base_options,
                                               num_hands=2)
        self.detector = vision.HandLandmarker.create_from_options(self.options)

    def evaluate(self, frame):
        try:
            img_path = frame
            img_path = cv2.cvtColor(img_path, cv2.COLOR_RGB2BGR)
            img_path = mp.Image(mp.ImageFormat.SRGB, data=img_path)
            detection_result = self.detector.detect(img_path)
            return detection_result

        except IOError:
            print("Something went wrong")
            pass
