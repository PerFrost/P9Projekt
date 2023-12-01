from model_context import ModelContext
from media_pipe_strategy import MediaPipeStrategy
from camera import Camera
from commands import Commands
from gui import GUI

if __name__ == '__main__':

    # g = GUI()
    #
    #
    #
    # g.createWindow()

    cam = Camera()
    mpstrat = MediaPipeStrategy()
    model = ModelContext(mpstrat)
    cmd = Commands()
    while True:
        frame = cam.getFrame()
        if frame is not None:
            newFrame = model.strategy.evaluate(frame)

            hand_landmarks_list = newFrame.hand_landmarks

            if hand_landmarks_list and len(hand_landmarks_list[0]) > 8:
                tip_of_index_finger = hand_landmarks_list[0][8]

                x = tip_of_index_finger.x
                y = tip_of_index_finger.y


                cmd.move_laser_pointer(x, y)

