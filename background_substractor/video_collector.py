import sys
sys.path.append('.')

import cv2
import app_configuration as cfg



class VideoCollector:
    '''
    This class connects with the video source
    At first it will connect with the webcam.
    Turn it into abstract class later and inherit for the webcam
    
    '''

    def __init__(self) -> None:
        self.capture = None
        self.initialized = False

    def initialize(self, video_path=None):

        if video_path is None:
            self.capture = cv2.VideoCapture(0)
        else:        
            self.capture = cv2.VideoCapture(cfg.dirs['data'])

            # Check if the webcam is opened correctly
        if not self.capture.isOpened():
            raise IOError("Cannot open webcam")
        else:
            self.initialized = True

    def run(self):
        ret, frame = self.capture.read()

        if ret:
            return frame
        else:
            print('cant receive frame')


        
        
    