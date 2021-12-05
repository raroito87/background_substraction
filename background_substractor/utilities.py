import numpy as np
import cv2
from functools import wraps
from time import time

class Utilities:


    @staticmethod
    def display_2_frames(frame_0, frame_1):        
        numpy_horizontal_concat = np.concatenate((frame_0, frame_1), axis=1)
        cv2.imshow('', numpy_horizontal_concat)
        cv2.waitKey(0)

    @staticmethod
    def timing(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start = time()
            result = f(*args, **kwargs)
            end = time()
            print('Elapsed time: {}').format(end-start)
            return result
        return wrapper