from model_context import ModelContext
from Mediapipe.media_pipe_strategy import MediaPipeStrategy
from MMPose.mmpose_strategy import MMPoseStrategy
from camera import Camera
from commands import Commands

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
    while True:
        frame = cam.getFrame()
        if frame is not None:
            newFrame = model.strategy.evaluate(frame)

            hand_landmarks_list = newFrame

            if hand_landmarks_list and len(hand_landmarks_list) > 8:
                tip_of_index_finger = hand_landmarks_list[8]

                x = tip_of_index_finger[0]
                y = tip_of_index_finger[1]


                cmd.move_laser_pointer2(x, y)


            # hand_landmarks_list = newFrame.hand_landmarks
            #
            # if hand_landmarks_list and len(hand_landmarks_list[0]) > 8:
            #     tip_of_index_finger = hand_landmarks_list[0][8]
            #
            #     x = tip_of_index_finger.x
            #     y = tip_of_index_finger.y
            #
            #
            #     cmd.move_laser_pointer(x, y)

