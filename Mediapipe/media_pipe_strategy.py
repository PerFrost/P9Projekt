import mediapipe as mp
import cv2
from model_strategy import ModelStrategy

class MediaPipeStrategy(ModelStrategy):

    def __init__(self):
        mphands = mp.solutions.hands
        self.detector = mphands.Hands(max_num_hands=2)

    def evaluate(self, frame):
        try:
            img_path = frame
            img_path = cv2.cvtColor(img_path, cv2.COLOR_RGB2BGR)
            # img_path = mp.Image(mp.ImageFormat.SRGB, data=img_path)
            detection_result = self.detector.process(img_path)
            try:
                return "mediapipe", detection_result.multi_hand_landmarks[0].landmark
            except:
                return "mediapipe", []

        except IOError:
            print("Something went wrong")
            pass
