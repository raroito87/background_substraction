import numpy as np
import cv2

class Utilities:


    @staticmethod
    def display_2_frames(frame_0, frame_1):        
        numpy_horizontal_concat = np.concatenate((frame_0, frame_1), axis=1)
        cv2.imshow('', numpy_horizontal_concat)
        cv2.waitKey(0)