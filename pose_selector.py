from commands import Commands


class PoseSelector:

    def __init__(self):
        self.cmds = Commands()

    def select_pose(self, label, landmarks):

        match label:
            case 0:
                print("Open")
            case 1:
                print("Closed")
            case 2:
                self.cmds.move_laser_pointer(landmarks)
            case 3:
                self.cmds.next_slide()
            case 4:
                self.cmds.prev_slide()
            case default:
                return
