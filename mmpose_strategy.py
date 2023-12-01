from mmpose.apis import MMPoseInferencer
from mmpose.utils import register_all_modules
import cv2
from model_strategy import ModelStrategy

class MMPoseStrategy(ModelStrategy):
    def evaluate(self, frame):
        register_all_modules()

        config_file = 'mmpose/configs/hand_2d_keypoint/rtmpose/hand5/rtmpose-m_8xb256-210e_hand5-256x256.py'
        checkpoint_file = 'mmpose/data/rtmpose-m_simcc-hand5_pt-aic-coco_210e-256x256-74fb594_20230320.pth'
        model = MMPoseInferencer(pose2d=config_file, pose2d_weights=checkpoint_file,
                                 device='cuda')  # or device='cuda:0'

        try:
            img_path = frame
            results = model(img_path, return_vis=True)

            result = next(results)

            print(type(result['visualization'][0]))

            img3 = cv2.cvtColor(result['visualization'][0], cv2.COLOR_RGB2BGR)

            cv2.imshow('Window', img3)

            cv2.waitKey(1)

        except IOError:
            print("Suck it")

        cv2.destroyAllWindows()