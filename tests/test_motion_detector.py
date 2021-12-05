from background_substractor import Utilities
import cv2
import app_configuration as cfg
import numpy as np

def load_test_frames():
    frame_0 = cv2.imread(cfg.dirs['test_data'] + 'frame_0.png')
    frame_1 = cv2.imread(cfg.dirs['test_data'] + 'frame_1.png')


    assert isinstance(frame_0, np.ndarray)
    assert isinstance(frame_1, np.ndarray)

    #percent by which the image is resized
    scale_percent = 50

    #calculate the 50 percent of original dimensions
    width = int(frame_0.shape[1] * scale_percent / 100)
    height = int(frame_0.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    return cv2.resize(frame_0, dsize=dsize), cv2.resize(frame_1, dsize=dsize)

class TestMotionDetector:


    def test_detect_keypoints(self):
        frame_0, frame_1 = load_test_frames()
        Utilities.display_2_frames(frame_0, frame_1)
