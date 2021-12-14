This project is the implementation of my Master Thesis in Python.

MAIN STEPS
- for every frame we compute keypoints and its descriptors
- we match the descriptor to the ones of frame - 1 (previour frame)
- we sort the matches fro best to worse. Might apply so filter
- compute homography. Or prestective mtrix: 

JOURNAL

- Comparsion between keypoint detector speed. Best combination should be ORB keypoints with BIBLID descriptors.
- 

BIBLIOGRAPHY
- from keypoints to https://docs.opencv.org/4.x/d1/de0/tutorial_py_feature_homography.html
- homography or perspective matrix_ https://vivekseth.com/computer-vision-matrix-differences/


IMPROVEMENTS IDEAS

- to compute the motion maybe I can use only black and white images so it compute faster -> try on test case