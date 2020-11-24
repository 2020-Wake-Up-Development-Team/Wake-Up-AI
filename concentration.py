"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import cv2
from focus import GazeTracking

gaze = GazeTracking()

#if mp4 file url below if ip ip below
webcam = cv2.VideoCapture(0)
is_watching={0:"not_focusing",1:"focusing"}
watch = -1
while True:
    _, frame = webcam.read()

    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""
    
    if gaze.is_center():
        text = "focusing"
        watch = 1
    else:
        watch = 0
        text = "not looking"

    if cv2.waitKey(1) == 27:

    cv2.imshow("Demo", frame)   