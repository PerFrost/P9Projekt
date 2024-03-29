from mmpose.apis import MMPoseInferencer
from mmpose.utils import register_all_modules
import cv2
from model_strategy import ModelStrategy

class MMPoseStrategy(ModelStrategy):
    def __init__(self):
        register_all_modules()

        config_file = 'MMPose/mmpose/configs/hand_2d_keypoint/rtmpose/hand5/rtmpose-m_8xb256-210e_hand5-256x256.py'
        checkpoint_file = 'MMPose/mmpose/data/rtmpose-m_simcc-hand5_pt-aic-coco_210e-256x256-74fb594_20230320.pth'

        self.model = MMPoseInferencer(pose2d=config_file, pose2d_weights=checkpoint_file,
                                 device='cpu')

    def evaluate(self, frame):
        try:
            img_path = frame
            results = self.model(img_path)

            result = next(results)

            return result['predictions'][0][0]['keypoints']

        except:
            return []
