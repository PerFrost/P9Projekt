from model_context import ModelContext
from Mediapipe.media_pipe_strategy import MediaPipeStrategy
from MMPose.mmpose_strategy import MMPoseStrategy
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

        strategy = MediaPipeStrategy() if settings.model == "MediaPipe" else MMPoseStrategy()
        model = ModelContext(strategy)
        cmd = Commands()

        while True:
            frame = cam.getFrame()
            if frame is not None:
                hand_landmarks_list = model.strategy.evaluate(frame)
                landmark_fact = LandmarkFactory(hand_landmarks_list, settings).create_landmarks()


                if landmark_fact and len(landmark_fact) > 8:
                    tip_of_index_finger = landmark_fact[8]

                    x = tip_of_index_finger[0]
                    y = tip_of_index_finger[1]

                    if x < 10:
                        break

                    cmd.move_laser_pointer(x, y)
