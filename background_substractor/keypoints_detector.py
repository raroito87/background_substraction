import cv2

class KeypointsDetector:

    def __init__(self):
        self.orb_detector = None
        self.beblid_descriptor = None
        self.initialized = False

    def initialize(self, num_points=400, scale_factor=0.75):
        self.orb_detector = cv2.ORB_create(num_points)  
        self.beblid_descriptor = cv2.xfeatures2d.BEBLID_create(scale_factor)
        self.initialized = True
        return True 

    def detect_keypoints(self, frame):
        if not self.initialized:
            raise Exception
            
        kp = self.orb_detector.detect(frame, None)        
        kp, des = self.beblid_descriptor.compute(frame, kp)

        return kp, des