from background_substractor import Utilities, KeypointsDetector
import cv2
import app_configuration as cfg
import numpy as np
from time import time
from pprint import pprint


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

class TestKeypointsDetector:

        
    def test_initialized_fails(self):
        keypoints_detector = KeypointsDetector()
        try:
            keypoints_detector.detect_keypoints(None)
        except:
            print('exception catched')
            assert True

    # def test_detect_keypoints_surf(self):
    #     frame_0, frame_1 = load_test_frames()

    #     # going to try the SURF algorithm
    #     surf = cv2.xfeatures2d.SURF_create(400)

    #     # Find keypoints and descriptors directly
    #     kp_0, des_0 = surf.detectAndCompute(frame_0, None)
    #     kp_1, des_1 = surf.detectAndCompute(frame_1, None)

    #     print('detected kp: ', len(kp_0), len(kp_1))

    #     # draw the keypoints
    #     img_0 = cv2.drawKeypoints(frame_0,kp_0,None,(255,0,0))
    #     img_1 = cv2.drawKeypoints(frame_1,kp_1,None,(255,0,0))
    #     # Utilities.display_2_frames(img_0, img_1)

    def test_detect_keypoints_orb(self):
        frame_0, frame_1 = load_test_frames()

        # going to try the ORB algorithm
        orb = cv2.ORB_create(400)

        # Find keypoints and descriptors directly
        kp_0, des_0 = orb.detectAndCompute(frame_0, None)
        kp_1, des_1 = orb.detectAndCompute(frame_1, None)

        print('detected kp: ', len(kp_0), len(kp_1))

        # draw the keypoints
        img_0 = cv2.drawKeypoints(frame_0,kp_0,None,(255,0,0))
        img_1 = cv2.drawKeypoints(frame_1,kp_1,None,(255,0,0))
        #Utilities.display_2_frames(img_0, img_1)

    def test_detect_keypoints_beblid(self):
        #https://towardsdatascience.com/improving-your-image-matching-results-by-14-with-one-line-of-code-b72ae9ca2b73
        frame_0, frame_1 = load_test_frames()

        # going to try the BEBLID algorithm
        orb_detector = cv2.ORB_create(400)
        beblid_descriptor = cv2.xfeatures2d.BEBLID_create(0.75)

        # Find keypoints and descriptors directly
        kp_0= orb_detector.detect(frame_0, None)
        kp_0, des_0 = beblid_descriptor.compute(frame_0, kp_0)

        kp_1= orb_detector.detect(frame_1, None)
        kp_1, des_1 = beblid_descriptor.compute(frame_1, kp_1)

        print('detected kp: ', len(kp_0), len(kp_1))

        # draw the keypoints
        img_0 = cv2.drawKeypoints(frame_0,kp_0,None,(255,0,0))
        img_1 = cv2.drawKeypoints(frame_1,kp_1,None,(255,0,0))
        #Utilities.display_2_frames(img_0, img_1)

    # def test_orb_faster_than_surf(self):
    #     # Can't run this test because SURF is not available in this opencv version
    #     # but in different one it was proven that SURF is slower than ORB    
    #     frame_0, frame_1 = load_test_frames()

    #     orb = cv2.ORB_create(400)
    #     start = time()
    #     kp_0, des_0 = orb.detectAndCompute(frame_0, None)
    #     orb_time = time() - start

    #     surf = cv2.xfeatures2d.SURF_create(400)
    #     start = time()
    #     kp_0, des_0 = surf.detectAndCompute(frame_0, None)
    #     surf_time = time() - start

    #     print('orb ', orb_time, ', surf ', surf_time)

    #     assert surf_time > orb_time

    def test_beblid_faster_than_orb(self):        
        frame_0, frame_1 = load_test_frames()

        orb = cv2.ORB_create(400)
        start = time()
        kp_0, des_0 = orb.detectAndCompute(frame_0, None)
        orb_time = time() - start


        beblid_descriptor = cv2.xfeatures2d.BEBLID_create(0.75)
        start = time()
        kp_0= orb.detect(frame_0, None)
        kp_0, des_0 = beblid_descriptor.compute(frame_0, kp_0)
        biblid_time = time() - start

        print('orb ', orb_time, ', biblid ', biblid_time)

        assert orb_time > biblid_time

    def test_get_keypoints(self):
        frame_0, frame_1 = load_test_frames()

        keypoint_detector = KeypointsDetector()
        assert keypoint_detector.initialize()

        kp, des = keypoint_detector.detect_keypoints(frame_0)
        
        assert isinstance(kp, tuple)
        assert isinstance(des, np.ndarray)
        assert len(kp) == len(des)
