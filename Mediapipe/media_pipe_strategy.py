import mediapipe as mp
from model_strategy import ModelStrategy

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
