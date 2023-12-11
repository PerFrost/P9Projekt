from model_context import ModelContext
from Mediapipe.media_pipe_strategy import MediaPipeStrategy
from MMPose.mmpose_strategy import MMPoseStrategy
from MMPose.mmpose_strategy2 import MMPoseStrategy2
from camera import Camera
from commands import Commands
from settings import Settings
from landmark_factory import LandmarkFactory
from gui import GUI

if __name__ == '__main__':
    while True:
        g = GUI()
        settings = g.createWindow()

        cam = Camera()

        strategy = MediaPipeStrategy() if settings.model == "MediaPipe" else MMPoseStrategy() if settings.model == "MMPose" else MMPoseStrategy2()
        model = ModelContext(strategy)
        cmd = Commands(settings)
        landmark_fact = LandmarkFactory(settings)

        while True:
            frame = cam.getFrame()
            if frame is not None:
                hand_landmarks_list = model.strategy.evaluate(frame)
                landmarks_cam = landmark_fact.create_landmarks_for_camera_res(hand_landmarks_list)
                landmarks_screen = landmark_fact.create_landmarks_for_screen_res(hand_landmarks_list)
                landmarks_calibrated = landmark_fact.create_landmarks_for_calibration(hand_landmarks_list)

                if landmarks_calibrated:
                    cmd.move_laser_pointer(landmarks_calibrated)
