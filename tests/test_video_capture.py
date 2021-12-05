from background_substractor import VideoCollector
import numpy as np
import app_configuration as cfg


class TestVideoCollector:

    def test_initialized(self):
        video_capture = VideoCollector()
        video_capture.initialize(video_path=cfg.dirs['data'] + 'test_1.mp4')

        assert video_capture.initialized

        frame = video_capture.run()
        assert isinstance(frame, np.ndarray)