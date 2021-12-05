from background_substractor import Utilities
import cv2
import app_configuration as cfg
import numpy as np
from time import time

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

    def test_detect_keypoints_surf(self):
        frame_0, frame_1 = load_test_frames()

        # going to try the SURF algorithm
        surf = cv2.xfeatures2d.SURF_create(400)

        # Find keypoints and descriptors directly
        kp_0, des_0 = surf.detectAndCompute(frame_0, None)
        kp_1, des_1 = surf.detectAndCompute(frame_1, None)

        print('detected kp: ', len(kp_0), len(kp_0))

        # draw the keypoints
        img_0 = cv2.drawKeypoints(frame_0,kp_0,None,(255,0,0))
        img_1 = cv2.drawKeypoints(frame_1,kp_1,None,(255,0,0))
        # Utilities.display_2_frames(img_0, img_1)

    def test_detect_keypoints_orb(self):
        frame_0, frame_1 = load_test_frames()

        # going to try the ORB algorithm
        orb = cv2.ORB_create(400)

        # Find keypoints and descriptors directly
        kp_0, des_0 = orb.detectAndCompute(frame_0, None)
        kp_1, des_1 = orb.detectAndCompute(frame_1, None)

        print('detected kp: ', len(kp_0), len(kp_0))

        # draw the keypoints
        img_0 = cv2.drawKeypoints(frame_0,kp_0,None,(255,0,0))
        img_1 = cv2.drawKeypoints(frame_1,kp_1,None,(255,0,0))
        #Utilities.display_2_frames(img_0, img_1)

    def test_orb_fatser_than_surf(self):        
        frame_0, frame_1 = load_test_frames()

        start = time()
        orb = cv2.ORB_create(400)
        kp_0, des_0 = orb.detectAndCompute(frame_0, None)
        orb_time = time() - start

        start = time()
        surf = cv2.xfeatures2d.SURF_create(400)
        kp_0, des_0 = surf.detectAndCompute(frame_0, None)
        surf_time = time() - start

        print('orb ', orb_time, ', surf ', surf_time)

        assert surf_time > orb_time
