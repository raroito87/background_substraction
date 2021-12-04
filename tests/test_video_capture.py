from background_substractor import VideoCollector


class TestVideoCollector:

    def test_initialized(self):
        video_capture = VideoCollector()
        video_capture.initialize()

        assert video_capture.initialized

        frame = video_capture.run()
        print('frame is type: ')
        print(type(frame))
        assert True