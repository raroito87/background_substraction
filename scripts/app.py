import cv2

from background_substractor import VideoCollector


if __name__ == '__main__':

    video_collector = VideoCollector()
    video_collector.initialize()


    finished = False
    while not finished:

        frame = video_collector.run()
        print('frame is type: ')
        print(type(frame))

        cv2.imshow('frame', frame)
        keyboard = cv2.waitKey(1)
        print('I pressed', keyboard)

        if keyboard == 32:
            finished = True

