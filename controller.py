from model_context import ModelContext
from Mediapipe.media_pipe_strategy import MediaPipeStrategy
from MMPose.mmpose_strategy import MMPoseStrategy
from camera import Camera
from commands import Commands
from landmark_factory import LandmarkFactory
from gui import GUI
from pose_recognizer import PoseRecognizer
from pose_selector import PoseSelector

if __name__ == '__main__':
    while True:
        g = GUI()
        settings = g.createWindow()

        cam = Camera()

        strategy = MediaPipeStrategy() if settings.model == "MediaPipe" else MMPoseStrategy()
        model = ModelContext(strategy)
        cmd = Commands()
        landmark_fact = LandmarkFactory()
        model_path = "Model/keypoint_classifier.tflite"
        pose_recog = PoseRecognizer(model_path)
        pose_select = PoseSelector()

        while True:
            frame = cam.getFrame()
            if frame is not None:
                hand_landmarks_list = model.strategy.evaluate(frame)
                landmarks_calibrated = landmark_fact.create_landmarks_for_calibration(hand_landmarks_list)
                hand_landmarks_list2 = landmark_fact.create_landmarks_for_screen_norm(hand_landmarks_list)

                if hand_landmarks_list2:
                    index = pose_recog(hand_landmarks_list2)
                    pose_select.select_pose(index, landmarks_calibrated)
