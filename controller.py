from model_context import ModelContext
from Mediapipe.media_pipe_strategy import MediaPipeStrategy
from MMPose.mmpose_strategy import MMPoseStrategy
from camera import Camera
from commands import Commands
from settings import Settings
from landmark_factory import LandmarkFactory

if __name__ == '__main__':

    # g = GUI()
    #
    #
    #
    # g.createWindow()

    cam = Camera()
    # mpstrat = MediaPipeStrategy()
    mmstrat = MMPoseStrategy()
    model = ModelContext(mmstrat)
    cmd = Commands()
    settings = Settings()

    while True:
        frame = cam.getFrame()
        if frame is not None:
            hand_landmarks_list = model.strategy.evaluate(frame)
            landmark_fact = LandmarkFactory(hand_landmarks_list, settings).create_landmarks()


            if landmark_fact and len(landmark_fact) > 8:
                tip_of_index_finger = landmark_fact[8]

                x = tip_of_index_finger[0]
                y = tip_of_index_finger[1]


                cmd.move_laser_pointer(x, y)