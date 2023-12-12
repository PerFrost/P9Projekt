import tensorflow as tf
import numpy as np

class PoseRecognizer():
    def __init__(self, model_path):
        self.model_path = model_path
        self.interpreter = tf.lite.Interpreter(model_path)
        self.interpreter.allocate_tensors()
        self.input_details_tensor_index = self.interpreter.get_input_details()[0]['index']
        self.output_details_tensor_index = self.interpreter.get_output_details()[0]['index']


    def __call__(self, landmark_list):
        self.interpreter.set_tensor(self.input_details_tensor_index, np.array([landmark_list], dtype=np.float32))
        self.interpreter.invoke()
        result = self.interpreter.get_tensor(self.output_details_tensor_index)
        return np.argmax(np.squeeze(result))