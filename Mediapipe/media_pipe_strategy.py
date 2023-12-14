import mediapipe as mp
import cv2
from model_strategy import ModelStrategy
import copy

class MediaPipeStrategy(ModelStrategy):

    def __init__(self):
        mp_hands = mp.solutions.hands
        self.detector = mp_hands.Hands(max_num_hands=2)

    def evaluate(self, frame):
        try:
            img_path = frame
            detection_result = self.detector.process(img_path)

            return detection_result.multi_hand_landmarks[0].landmark

        except:
            return []
