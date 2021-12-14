import cv2


class DescriptorMatcher:

    def __init__(self) -> None:        
        self.initialized = False
        self.matcher = None

    def initialize(self):
        self.initialize = True
        self.matcher = cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_BRUTEFORCE_HAMMING)
        return True

    def match_descriptors(self, des1, des2):
        if not self.initialized:
            raise Exception

        return True


