from background_substractor import DescriptorMatcher



class TestDescriptorMatcher:

    def test_initialized_fails(self):
        keypoints_detector = DescriptorMatcher()
        try:
            DescriptorMatcher.match_descriptors(None, None)
        except:
            print('exception catched')
            assert True


    def test_matching_quality(self):
        '''
        test the quality of matches between Brute Force and Flann
        '''
        pass
    

    def test_matching_speed(self):
        '''
        test the speed of both matching algorithms
        '''
        pass