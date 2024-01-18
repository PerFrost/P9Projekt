from commands import Commands


class PoseSelector:

    def __init__(self):
        self.cmds = Commands()
        self.current_hand_pose = 0
        self.previous_hand_poses = [0 for _ in range(5)]
        self.laser_pointer_toggle = False

    def select_pose(self, label, landmarks):
        self.previous_hand_poses.pop(0)
        self.previous_hand_poses.append(label)

        most_frequent_hand_pose = self.most_frequent_hand_pose()
        if most_frequent_hand_pose != self.current_hand_pose:
            self.current_hand_pose = most_frequent_hand_pose

            if self.laser_pointer_toggle:
                self.laser_pointer_toggle = False
                self.cmds.toggle_laser_pointer()

            match most_frequent_hand_pose:
                case 0:
                    print("Open")
                case 1:
                    print("Closed")
                case 2:
                    self.laser_pointer_toggle = True
                    self.cmds.toggle_laser_pointer()
                case 3:
                    self.cmds.next_slide()
                case 4:
                    self.cmds.prev_slide()
                case default:
                    return

        if self.current_hand_pose == 2:
            self.cmds.move_laser_pointer(landmarks)

    def most_frequent_hand_pose(self):
        counts = [0 for _ in range(5)]
        for x in self.previous_hand_poses:
            counts[x] += 1

        return counts.index(max(counts))