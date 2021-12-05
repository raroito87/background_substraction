# PROBLEM : I can run this script with Run-> run without debugging If I run it in terminal my custom module is not foud.
# I can also run pytest and the custom modules are founs
# Termporary workaround: add upper path. https://stackoverflow.com/questions/62913803/vscode-do-not-find-my-custom-python-package
# For some reason if I dont append this,The cutom modules are not found
# Seems like the working directory is not the project root but the script directory when  run it with the terminal
import sys
sys.path.append('.')

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

