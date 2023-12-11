from mmpose.apis import MMPoseInferencer
from mmpose.utils import register_all_modules
import cv2
from model_strategy import ModelStrategy

class MMPoseStrategy2(ModelStrategy):
    def __init__(self):
        register_all_modules()

        config_file = 'MMPose/mmpose/configs/hand_2d_keypoint/rtmpose/coco_wholebody_hand/rtmpose-m_8xb32-210e_coco-wholebody-hand-256x256.py'
        checkpoint_file = 'MMPose/mmpose/data/rtmpose-m_simcc-coco-wholebody-hand_pt-aic-coco_210e-256x256-99477206_20230228.pth'
        self.model = MMPoseInferencer(pose2d=config_file, pose2d_weights=checkpoint_file,
                                 device='cpu')  # or device='cuda:0'

    def evaluate(self, frame):
        try:
            img_path = frame
            results = self.model(img_path) #, return_vis=True)

            result = next(results)

            # self.visualize(result)

            return result['predictions'][0][0]['keypoints']

        except:
            return []

    def visualize(self, result):
        img3 = cv2.cvtColor(result['visualization'][0], cv2.COLOR_RGB2BGR)

        cv2.imshow('Window', img3)

        cv2.waitKey(1)