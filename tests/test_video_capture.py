from background_substractor import VideoCollector
import numpy as np


class TestVideoCollector:

    def test_initialized(self):
        video_capture = VideoCollector()
        video_capture.initialize()

        assert video_capture.initialized

        frame = video_capture.run()
        assert isinstance(frame, np.ndarray)